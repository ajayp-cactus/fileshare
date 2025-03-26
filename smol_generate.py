# Prerequisites:
# pip install vllm
# pip install docling_core
# place page images you want to convert into "img/" dir

import time
import os
from vllm import LLM, SamplingParams
from PIL import Image
from docling_core.types.doc import DoclingDocument
from docling_core.types.doc.document import DocTagsDocument

# Configuration
MODEL_PATH = "ds4sd/SmolDocling-256M-preview"
IMAGE_DIR = "/home/ajay_prakash/smol_docling_outputs/images/"  # Place your page images here
OUTPUT_DIR = "/home/ajay_prakash/smol_docling_outputs/"
PROMPT_TEXT = "Convert page to Docling."

# Ensure output directory exists
# os.makedirs(OUTPUT_DIR, exist_ok=True)

# Initialize LLM
llm = LLM(model=MODEL_PATH, limit_mm_per_prompt={"image": 1})

sampling_params = SamplingParams(
    temperature=0.0,
    max_tokens=8192)

chat_template = f"<|im_start|>User:<image>{PROMPT_TEXT}<end_of_utterance>Assistant:"

import glob

file_list=glob.glob(IMAGE_DIR+"/*")

for im_file in sorted(file_list):
    print(im_file)
    start_time = time.time()
    
    try:

        image_files = sorted([f for f in os.listdir(im_file) if f.lower().endswith((".png", ".jpg", ".jpeg"))])

        total_tokens = 0

        doctags=[]
        images=[]
        
        for idx, img_file in enumerate(image_files, 1):
            img_path = os.path.join(im_file, img_file)
            image = Image.open(img_path).convert("RGB")
            images.append(image)

            llm_input = {"prompt": chat_template, "multi_modal_data": {"image": image}}
            output = llm.generate([llm_input], sampling_params=sampling_params)[0]
            
            doctags.append(output.outputs[0].text)
        img_fn = os.path.splitext(im_file)[0].split("/")[-1]
        output_filename = img_fn + ".dt"
        output_path = os.path.join(OUTPUT_DIR, output_filename)
        print(img_fn,output_filename,output_path)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write("\n".join(doctags))

        # To convert to Docling Document, MD, HTML, etc.:
        doctags_doc = DocTagsDocument.from_doctags_and_image_pairs("\n".join(doctags), images)
        doc = DoclingDocument(name="Document")
        doc.load_from_doctags(doctags_doc)
        # export as any format
        # HTML
        # doc.save_as_html(output_file)
        # MD
        output_filename_md = img_fn + ".md"
        output_path_md = os.path.join(OUTPUT_DIR, output_filename_md)
        doc.save_as_markdown(output_path_md)
    except Exception as e:
        print(im_file,"FAILED")

    print(f"Total time {img_fn}: {time.time() - start_time:.2f} sec")

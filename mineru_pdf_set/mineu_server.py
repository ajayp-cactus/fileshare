
import requests

import glob
output_dir="/home/ajay_prakash/fileshare/mineru_pdf_set/output/"
dir="/home/ajay_prakash/fileshare/mineru_pdf_set/"
files_list=glob.glob("{}*.pdf".format(dir))


 
import time
times=[]
pdf_ids=[]
for file in sorted(files_list):
    try:
        start=time.time()

        url = "http://0.0.0.0:8000/pdf_parse"
#        url = "http://0.0.0.0:8000/predict"
        payload = {"output_dir":output_dir+"/docker_output/"}
        files=[
        ('pdf_file',(file.split("/")[-1],open(file,'rb'),'application/pdf'))
#        ('file',(file.split("/")[-1],open(file,'rb'),'application/pdf'))
        ]
        headers = {
        }

        response = requests.request("POST", url, headers=headers, data=payload, files=files)

        with open(dir+file.split("/")[-1].split(".")[0]+".md","w") as f:
            f.write(response.text)
            f.close()
        # print(response.text)
        # pdf_ids.append(response.json()["pdf_id"])
            
            
        print(file,time.time()-start)
        times.append(time.time()-start)
    except Exception as e:
        print(file,e)    
    # break
        

print("final ",sum(times)/len(times))


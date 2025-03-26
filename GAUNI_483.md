## Toward Dynamic Energy Management for Green Manufacturing Systems

Eunsung Oh and Sung-Yong Son

## ABSTRACT

The authors discuss how dynamic energy management in manufacturing systems can not only solve the current technical issues in manufacturing, but can also aid in the integration of additional energy equipment into energy systems. They quantitatively estimate these potential savings through analysis of a simple manufacturing process. They also address a future research direction, wherein advanced manufacturing systems such as Industry 4.0 are deployed.

The manufacturing industry is responsible for significant energy consumption, particularly in the form of electricity. From the perspective of the energy management system in manufacturing, reducing this consumption is not only a matter of exhibiting environmental responsibility, but also of substantially reducing the production cost. We discuss how dynamic energy management in manufacturing systems can not only solve the current technical issues in manufacturing, but can also aid in the integration of additional energy equipment into energy systems. We quantify, but can also aid in the integration of additional energy equipment into energy systems. We quantitatively estimate these potential savings through analysis of a simple manufacturing process. We also address a future research direction, wherein advanced manufacturing systems such as Industry 4.0 are deployed.

## INTRODUCTION

For the maintenance of human life and sustainable economic progress, energy is crucial. The increase in energy demand is raising awareness about the potential harmful effects of CO$\_{2}$ emissions on the environment. There is growing consensus on the need to develop efficient and low-carbon technologies in all sectors, including energy supply, energy transformation, and energy consuming sectors such as buildings, industry, transport, and agriculture. It is important to note that the world's annual industrial energy consumption is high to the total energy consumption BTU (26 quadrillion BTU) including electricity losses (in 2011, which is 51 percent of the total energy consumption [1]).

Although industry is a high consumer of energy, the effect of energy consumption has been less interest, especially in manufacturing. There are two reasons for this; first, the energy consumed during production is underestimated. It is estimated that the energy cost amounts to about 4-10 percent of the value added in the manufacturing sector [2]. The other reason is the difficulty of energy management. It is very hard to store and immediately change the state of energy. Furthermore, different characteristics of variable energy sources make energy control a complex problem. Consequently, manufacturers have focused on reliable and efficient production rather than increasing energy efficiency. However, the additional energy costs related to institutional regulations for achieving the Kyoto Protocol goals (e.g.,

carbon credit quotes about carbon dioxide and greenhouse gases (GHGs) keep increasing [3]. Therefore, the discussion on energy efficiency in manufacturing cannot be put off indefinitely.

The energy consumption in manufacturing systems consists of two parts: "production" and "utility." Consumption attributed to production is directly related to the processes and operations involved in making the actual goods using manufacturing facilities. Utility consumption includes not only consumption due to the infrastructure that indirectly supports the production process, such as electricity, heat, and air.

The energy efficiency for production is correlated with productivity improvement. Improving the utilization rate of production equipment reduces unnecessary energy consumption during standby time, while reducing the task time also enhances the energy efficiency by decreasing the energy usage while producing the same amount of goods. Most of the studies that have considered the topic of energy efficiency have focused on energy per productive output ratio in the production system [4]. Moreover, through the development of intelligent manufacturing systems, known as Industry 4.0 or Smart Factory [5], coordinated by information networks, the research on increasing production efficiency has accelerated. This is because the purpose of the manufacturing system is to produce excellent value-added products. Industry 4.0, which is recently trending in the industry, presents a smart factory that supports more intelligent and agile manufacturing to meet the more rapid changes in consumers' requirements. Energy efficiency is one of the important objectives of the smart factory in view of cost effectiveness as well as social requirements. From this viewpoint, green manufacturing is also an important cost of organizing a smart factory.

The security of the energy supply should be satisfied without reducing the productivity, as well as the energy saving when considering the energy efficiency problem in manufacturing. In this respect, there are various efforts being made to improve the energy efficiency of the manufacturing system jointly considering the energy operation, and a new attempt is being made. In this article, we primarily discuss these techniques and issues.

The other part of energy consumption for the utility becomes base load. Base load consump- tion adds zero value to products and GHG emis-

<!-- image -->

Figure 1. Green manufacturing environment and its evolution from the perspective of electricity. sions. The base load cannot easily be reduced because it is related to the manufacturing infrastructure. The base load of the manufacturing not only uses its own energy sources, such as heat and air generation, but also uses the electricity transmitted from outside energy sources. Specifically, electricity consumption is continuously increased because of its availability and service-ability. The electricity is mainly generated by a non-renewable source, so the generation and consumption of electricity affects the social cost, which is related to not only the manufacturing system, but also other social systems. For example, increasing the peak demand, which is one of the parameters used to measure electricity consumption, results in the use of the expensive and less effective generator, which results in high GHG emissions. For green manufacturing, the effective control of energy sources, as well as its own greening, should be considered.

Green manufacturing covers a wide range of environmental and sustainability issues including resource material selection, transportation, manufacturing process, pollution, and so on. [6] The introduction of Industry 4.0 makes energy efficiency issues for manufacturing more practical, and there have been some efforts to reduce the total energy consumption in the manufacturing process [7]. However, the dynamic nature of energy and load has been not sufficiently considered yet.

In this article, we explore energy management mechanisms for manufacturing systems to understand the energy control not only for production, but also for utility. The main goal of this article is to introduce the potential gain when applying the technologies researched in energy systems into manufacturing systems considering their characteristics. We first address the techniques that can be applied to current green manufacturing and their related issues. Using simple algorithms, we estimate the potential gain by improving the energy efficiency expressed as the energy cost saving, based on a real production activity log and energy data in the analysis. We finally suggest the challenges for a more advanced way, particularly to ensure that energy efficiency does not come at the expense of reduced sustainable productivity.

The article is divided into three additional sections. In the following section, we discuss

related techniques and issues for green manufacturing. Then we present a first-order analysis on the scope of potential energy efficiency enhancement through green energy management. Lastly, we present the future methodology and conclude our findings.

## TECHNOLOGIES AND ISSUES OF

## GREEN MANUFACTURING

To achieve green manufacturing in terms of electricity, manufacturers should consider demand charge and energy charge, which are the main electricity bill components. The importance of reducing the energy charge is obvious. Meanwhile, it is also meaningful to reduce the demand charge because a high demand charge implicitly means high social energy costs.

In this section, methodologies for green manufacturing are classified, and their issues are discussed. In particular, we discuss issues related to manufacturing systems, address more advanced technical issues, and discuss the required additional equipment. Figure 1 shows a green manufacturing environment that consists of a main production process, supporting utilities, and other advanced energy resources. Each character from A to F presented within a circle is explained in the following corresponding subsections.

## UNIT FACILITY EFFICIENCY IMPROVEMENT

This is the most obvious and preferred methodology to achieve energy efficiency. However, energy efficiency is usually not a key decision factor for facility selection or change. Once a facility is installed, it is not easy to replace because of the loss during change, and there can be unknown risks until the entire system is stabilized again.

## UTILITY CONTROLS FOR ENARGY SAWINGS

The cost of energy in industry is low compared to the value added via the manufacturing process. Therefore, people give a higher priority to manufacturing planning to meet the required shipment schedule compared to energy efficiency in the field. Utility that supports a manufacturing process is essential, but has limited influence on the production process, and is usually an easy target to improve energy efficiency. Although

To achieve green manufacturing in terms of electricity, manufacturers should consider demand charge and energy charge, which are the main electricity bill components. The importance of reducing the energy charges is obvious. Meanwhile, it is also meaningful to reduce the demand charge because a high demand charge implicitly means high social energy costs.

## COMBINE AND HEAT AND GENERATION OPERATION

Combined heat pumps are often introduced because heat is one of the most common energy forms required in the industry, along with electricity [8]. The optimal simultaneous utility. of heating and electricity has been a long-term research issue, and its importance keeps increasing for achieving improved total energy efficiency.

## ADOPTING RENEWALES TO REDUCE CO$\_{2}$ EMISSION

The greening pressure on industry will keep increasing because of the industry's high energy consumption density compared to residen- tial and commercial energy consumption. Such trends have driven the widespread development and installment of photovoltaic panels on factory roofs and parking lots. These renewable energy technologies contribute to the reduction of energy charges and CO$\_{2}$ emissions [9]. However, these resources have variations and difficulties in predicting the output characteristics that may cause region power supply instability. Although photovoltaic may contribute to reducing the demand charge, in most cases, because the generation matches grid peak time, it cannot guard- ante the contribution. This is because one day of cloudy weather can determine high energy charges. Electric energy storage (EES) is one of the potential solutions. However, the high initial capital cost should be overcome.

## ACTIVE RESOURCES FOR PEAK CUTTING

Peak cutting is not just for the purposes of energy cost reduction of individual manufacturers, but is also part of the overall development of green technology on a national scale. Many manufacturing industries have intermittently high short-term energy consumption processes that result in high demand charges. EES is considered as the recent improvement of EES technology enables a fast response to compensate for the peak reduction. The high cost of EES prevents adopting EES as an energy shifting or demand response. However, intermittent peak cutting can be implemented relatively small amounts of EES; the economic feasibility can be acquired. The appropriate size of the EES is important in this approach, and there are many studies in this area.

## CO-OPTIMIZATION OF

## MANUFACTURING PLANNING AND ENERGY MANAGEMENT

Manufacturing execution planning focuses on efficient and reliable production scheduling, which considers resource, facility, and other production-related factors. Although the manufacturing execution plan affects electricity usage patterns, it was not the main concern in the planning process. It is recently considered to combine or co-optimize manufacturing execution planning with an energy management that focuses on energy savings in industry[10, 11]. However, planning complexity and unknown risks prevent the approach from being widely accepted at present. When considering time-varying electricity prices, manufacturing execution planning will

consider energy consumption considerations more seriously in the long term.

The unit facility efficiency improvement is directly related to the process efficiency, but has limited effect on the impact range. The utility control and the combined heat and generation operation indirectly affect the manufacturing process, and the range of the impact is broad. The adoption of renewables and active resources results in similar characteristics as the supporting utilities; however, it has higher variability and requires management that is more advanced. The co-optimization of manufacturing and energy management is one of the ultimate goals of green manufacturing, integrating all of the above approaches into one organic system.

In the manufacturing environment, combining new energy resources increases the operation complexity. In particular, renewable energy resources are difficult for forecasting and control because of their energies: active resources such as energy storage systems require continuous control. Such manufacturing environmental changes require an integrated operation that considers the manufacturing plans, situation of shop floors, and status of energy resources, all together in real time, to pursue green manufacturing. This means that a reliable and agile information network is essential. Figure 1 shows the information-network-based integrated aspects of the manufacturing execution system (MES) to plan and coordinate the production process, the point of product (POP) system to monitor and control facilities on the production floor, and the energy management system (EMS) and other supporting systems.

## A CASE STUDY

Energy in manufacturing is consumed for production and utility. Each method of consumption is related to the demand charges, which depend on the peak electricity load and the energy charge for the total electricity quantity, respectively. The major consideration for reducing these charges in the energy network aspect is EES and renewable resources, and it is also applied to the manufacturing system. In this section, we address a manufacturing process and its electricity load, and we estimate the degree of energy efficiency enhancement when the EES and renewable sources are applied to the system for reducing the peak load and the total amount of load. EES is an emerging and highly appropriated resource that can meet the uncertain changes in renewable generation and manufacturing responsiveness because of its ease of control and rapid responsiveness. Renewable sources reduce the use of conventional electric energy that comes from the grid, generated mostly by fossil fuels, making the manufacturing green. Therefore, this

The ENERGY DEMAND of a Manufacturing SYSTEM In Fig. 2a, the manufacturing process layout, including the production flow used for the case study, is shown. The flow represents a simplified manufacturing process with injection molding, machining, assembly, and painting. The process has four sequences with multiple machines to match the production cycle time between the pro-

resonances. Renewable sources reduce the use of conventional electric energy that comes from the grid, generated mostly by fossil fuels, making the manufacturing green. Therefore, this section focuses on the EES and renewable integration from among the other approaches.

## THE ENERGY DEMAND OF A MANUFACTURING SYSTEM

In Fig. 2a, the manufacturing process layout, including the production flow used for the case study, is shown. The flow represents a simplified manufacturing process with injection molding, machining, assembly, and painting. The process has four sequences with multiple machines to match the production cycle time between the pro-

<!-- image -->

<!-- image -->

Figure 2b shows the electricity consumption in active power for the manufacturing process. Time zones 1, 2, and 3 represent normal, trouble, and recovery cases, respectively. In time zone 1, intermittent peaks can be observed because of the injection molding process. To calculate the energy consumption as a function of time, the detailed production flow is simulated using a Monte Carlo simulation. Based on the production flow, the energy consumption of each machine is obtained using the energy consumption pattern corresponding to the associated job for the machine. The total energy consumption values for every instance of time are obtained by aggregating the energy consumption of all facilities in sync. Two simulations are performed based on the operation scenarios with performed trouble to compare the difference. The red and blue lines in Fig. 2b show the energy consumption for the scenario.

The peaks appear periodically in the normal or ideal condition, even though they would be somewhat dispersed in reality. The base load during manufacturing looks relatively high because the base load is the mix of accumulated manufacturing process loads and utility loads. The power consumption can be roughly estimated from the manufacturing execution plan by matching it with the energy consumption of the individual process. In time zone 2, process trouble in the injection molding process is introduced at time 1000 min to observe the effect of a contingency, and it is assumed that the trouble

plan focuses on early recovery of the manufacturing system. The new peak would bring a negative long-term effect to the demand charge.

## Peak Cutting UNDER EES OPERATIONS FOR THE PRODUCTION SYSTEM

As shown in time zone 1 of Fig. 2b, the periodic peak loads appear during the normal process, and in zone 3 an abnormal peak load arises following an unexpected event. The peak load reduces the reliability of energy supply, which not only results in reduced energy efficiency, but also worsens the life of the manufacturing equipment. A relevant approach to managing the peak load is the usage of EES. In the application of EES sizing is the essential problem because the EES size limits the degree of freedom for the operation. Various methods based on stochastic approaches have been discussed for EES sizing because of price and load uncertainty in energy systems [12]. In order to solve the problem based on the stochastic approach, probabilistic modeling should be estab-lished. The difference of the load characteristic between the energy system and the manufacturing system makes application of the researched EES techniques for energy systems into the manufacturing systems hard. However, it is known that load in manufacturing is consumed under the process schedule, and it is periodically worked. To control the periodical load, discrete Fourier transform (DFT)-based EES sizing is effective [13].

The basic idea behind DFT-based EES sizing for peak load cutting uses the assumption that

Each method of consumption is related to the demand charges, which depend on the peak electricity load and the energy charge about the total electricity quantity, respectively. The major consideration for reducing these charges in the energy network aspect is EES and renewable resources, and it is also applied to the manufacturing system.

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->
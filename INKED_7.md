<!-- image -->

## Contents lists available at ScienceDirect

## Applied Energy

journal homepage: www.elsevier.com/locate/apeenergy

## Metaheuristic optimization methods for a comprehensive operating schedule of battery, thermal energy storage, and heat source in a building energy system

Shintaro Ikeda $^{a,}$*, Ryozo Ooka b

$^{a}$Department of Architecture, The University of Tokyo, 4-6-1 Komaba, Meguro-ku, Tokyo 153-8505, Japan

$^{b}$Institute of Industrial Science, The University of Tokyo, 4-6-1 Komaba, Meguro-ku, Tokyo 153-8505, Japan

## HIGH LIG HTS

We proposed metaheuristic optimization methods for energy systems.

The proposed method, m-PSO can calculate the optimal solution quickly and accurately.

The proposed method can find a solution 6,206,88 times as fast as previous method.

The proposed methods can solve nonlinear and non-differentiable problems quickly.

## ARTICLE INFO

Article history:

Received 14 October 2014

Received in revised form 27 February 2015

Accepted 8 April 2015

Keywords:

Metaheuristics

Cuckoo search

m-PSO

Dynamic programming

Battery

Thermal energy storage

## 1. Introduction

In recent years, renewable power generators, such as wind turbines (WTs) and photovoltaics (PVs), have been increasingly installed in energy grids owing to feed-in tariffs and declining installation costs. The number of installations of renewable power generators is expected to increase [1]. Storage equipment has been installed with WT or PV to avoid electric grid fluctuation and intermittency [2]. In addition, batteries have a significant role in reducing operating costs in the building sector. Thermal energy storage (TES) with combined heat and power (CHP) and heat pump

* Corresponding author. Tel.: +81 3 5452 643; fax: +81 3 5452 643.

E-mail addresses: -s likeda.i@us-tokyo.ac.jp, (S. Ikeda.)

0306-2619/© 2015 Elsevier Ltd. All rights reserved.

has a similar role in that sector. Although optimal operation is important in maximizing their roles, it is a complex problem, because there are many things to consider when optimizing their operation, such as outdoor temperature, machine characteristics, and the price of electricity. Therefore, it is important to study energy system optimization.

There have been many previous studies of this topic [3-10]. Omu et al. [3] used mixed-integer linear programming (MILP) to minimize annual investment and operating costs of a distributed energy system. Basu and Chowdhury [4] used the cuckoo search (CS) algorithm to optimize economic dispatch problems of generators on a microgrid. Chandrasekaran and Simon [5] used CS to solve the unit commitment problem (UCP) and economic dispatch problem (EDP) using a fuzzy algorithm. Fazlollahi and Marechal [6] proposed a hybrid method with an evolutionary algorithm and MILP

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

Amount of charging/discharging of electricity in warming up period [KW] Amount of charging/discharging of electricity in analyzed period [KW] ---- The state of charge in warming up period [KWh] ---- The state of charge in analyzed period [kWh]

<!-- image -->

Operating time intervals, because finding the solutions of m-PSO is not enough for convergence in the warming up period. However, the discharging operation at 12, 1, and 5 a.m. in warming up period

<!-- image -->

<!-- image -->

<!-- image -->

vanished in the analyzed period (green bar charts) because of the recalculation of optimization. In terms of discharging, each of the three optimization methods is conducted according to similar operation schedules, namely discharging is conducted when the price of electricity is high during the day in the warming up and analyzed periods.

3.7.2. Optimal operation schedule of TES and AHP

The optimal operation schedules of TES and AHP are shown in Fig. 16. In the results of DP and CS, Fig. 16(a) and (c), although the capacity of AHP is 100-1100 kW depending on outdoor temperature, TES stores thermal energy around 450-500 kW at night time in both periods. The reason is that half power outputs of

- (2) We developed m-PSO, which improved on c-PSO by adding a mutation method for individual position and was superior to c-PSO and EPSO, which uses a mutation method for velocity determination.
- (3) The computational and convergence speeds of m-PSO were the highest. For SC-I, m-PSO can converge within 1% tolerance with a theoretically optimal solution of DP 52,068 times as fast as DP. For SC-II, we found that m-PSO can converge within 0.304% 23 times as fast as DP.
- (4) In terms of computational accuracy, CS is the most accurate. For SC-II, CS converged within 0.22% 13 times as fast as DP. For SC-III, CS converged within 0.062% 7 ten times as fast as DP.
- (5) A heat source machine (AHP) that had nonlinear COP characteristics was able to work with its highly efficient load rate (0.4-0.55). Therefore, the proposed methods were able to solve the nonlinear problem quickly while maintaining the computational accuracy.

Therefore, metaheuristics, particularly m-PSO and CS, have a substantial advantage over DP for optimizing the operating schedule of an energy system that includes a battery and TES.

## References

- [1] International Energy Agency (IEA). World Energy Outlook 2013 Chapter 6 Renewable Energy Outlook, 2013. p. 197-232.
- [2] Toshiba Corporation. Smart Grid Progress in Japan, US/US, Japan Renewable Energy Policy Business Roundtable, 2012. p. 10.
- [3] Omu A, Choudhary R, Boies A. Distributed energy resource system optimization using mixed integer linear programming. Energy Policy 2013:61:249-66.
- [4] Basu M, Chowdhury A. Cuckoo search algorithm for economic dispatch. Energy 2013:60:99-100.
- [5] Chandrasekaran K, Simon SP. Multi-objective scheduling problem: hybrid approach using fuzzy assisted cuckoo search algorithm. Swarm Evol. Comput. 2012:5:1-16.
- [6] Fazolali H, Marcel F. Multi-objective, multi-potential optimization of biomass conversion technologies using evolutionary algorithms and mixed integer linear programming (MILP). Appl Therm Eng 2013:n504-1504.
- [7] Fong K. Yuen, S. Chow, CK Long, SW Eng. Energy and Design of centralized air-conditioning systems through the non-reversible strategy for heuristic optimization methods. Appl Energy 2013:784-3496.
- [8] Lee W, Kus G, Kuning C. Optimization of heat pump system in indoor swimming pool using particle swarm algorithm. Appl Therm Eng 2008:26:1847-26:33.
- [9] Moradia MH, Hajnariz M, Baspar S, Iporun P. An energy management system (EMS) strategy for combined heat and power (CHP) systems based on hybrid optimization method. employing fuzzy programming. Energy 2013:49:68-19.
- [10] Wang J, Jing Y, Wang C. CF optimization of capacity and for CCHP systems based on system-by genetic algorithm. Appl Energy 2010:87:1325-35.
- [11] Ashouri A, Fux S, Benz MJ, Guzella L. Optimization design and operation of building services using mixed-integer linear programming techniques. Energy 2013:56:35-36.
- [12] Buoro D, Pinto-Banyani P. Remi Optimization of a Distributed Cogeneration System with solar district heating, Appl Energy 2014:12:389-38.
- [13] Dai R, Metsahbi O. Optimal power generation load management for off-grid hybrid power systems with renewables available via mixed-integer programming. Energy Convers Manage 2013:73:234-34.
- [14] Ikegami I, Iwagawa Y, Iognito M. Optimal Demand Controls for a Heat Pump Water Heater under Different Objective Functions. IEEE International Conference on Power System Technology (POWERCON), 2012. p. 1-6.
- [15] Vettler J, M. Cost-optimal design of an ice-storage cooling system using mixed-integer linear programming techniques under various electric tariff facilities. Energy Chem 2013:42:29-36.
- [16] Waku T, Kinostiha T, Yokoyama R. A mixed-integer linear programming approach for cooperation based residential energy supply networks with power and heat interchanges. Energy 2014:68:29-46.
- [17] Waku T, Wada N, Yokohama R. Energy-saving efficient design of a residential polymer electrolyte fuel cell generation system combined with a plug-in hybrid energy-cycle energy Convers Manage 2014:74:40-51.
- [18] Waku T, Yokoyama R. Optimal sizing of residential gas engine configuration system for interconnection operation energy-saving viewpoint. Energy 2013:31:366-316.
- [19] Waku T, Yokoyama R. Optimal structural design of residential gas engine systems in consideration of their operating restrictions. Energy 2014:64: 719-33.
- [20] Yun H, Li W. Optimization and analysis of distributed energy system with energy storage device. Energy Procedia 2011:12:958-65.
- [21] Facci AL, Andreassi L, Uberti Stefano, Scubba Enrico. Analysis of the influence of thermal energy storage on the optimal management of a trigeneration plant. Energy Procedia 2014:45:1259-304.
- [22] Chen HJ, Wang DWP, S.L. Optimization of an ice-storage air conditioning system using dynamic programming method. Appl Therm Eng 2005:25:461-72.
- [23] Li J, Danzer MA. Optimal charge control strategies for stationary photovoltaic battery systems. Power Sources 2014:258:365-73.
- [24] Abbey C, Struznak K, Jo Gs. A knowledge-based approach for control of two-level energy storage for wind energy systems. IEEE Trans Energy Convers 2009:24:25-539-47.
- [25] Bahmani-Firoiu B, Azizani-Paahagboeorge R. Optimal sizing of battery energy storage for micro-grid operation management using a new improved battery algorithm. Electrical Power Energy 2014:56:42-54.
- [26] Dwd MJ, Mohamed A, Pabriham AA, Hannan MA. Heuristic optimization of state-of-charge feedback controller parameters for output power dispatch of hybrid photovoltaic/battery energy storage system. Measurement 2014:49:15-25.
- [27] Bazewi A, Kavousi-Farad. Consider uncertainty in the optimal energy management of renewable micro-grids including storage devices. Renewable Energy 2013:59:155-68.
- [28] Lee W, Chen SY, VT WH. Optimization for ice-storage air-conditioning system using particle swarm algorithm. Appl Energy 2009:86:1589-95.
- [29] Moghaddam AA, Seifi A, Nikham T, Pahlavani MRA. Multi-objective operation management of a renewable energy (MIG-micro-grid) with back-up-micro-turbine fuel cell/battery hybrid power source. Energy 2011:36:460-507.
- [30] Pedrasa MA, Spooner TD, MacGilliff C. Coordinating schedule for distributed energy resources to optimize smart home energy services. IEEE Transactions Smart Grid 2010:1:21-134-43.
- [31] Wang J, Zhai J, Ziang J, Ying Z, Chang C. Particle swarm optimization for redundant building cooling heating power and solid power system. Appl Energy 2010:87:3688-769.
- [32] Bazewa-Żore S, Mohammadi K. Parameter optimization via cuckoo optimization algorithm of fuzzy controller for energy management of a hybrid power system. Energy Convers Manage 2014:208:767-83.
- [33] Ekren O, Ekren BY. Size optimization of a PV/wind hybrid energy conversion system with battery storage using simulated annealing. Appl Energy 2010:87:592-8.
- [34] Valen (Lo, Shooshemi M). The Effect of PHEV and HYD duty cycles on battery and battery pack performance. In: Proc.-Plug-in Highway Electric Vehicle Conference, 2007: p. 1-9.
- [35] BatteryPlusForLife. Battery Technology Comparison, 2014.
- [36] Dinner I, Rosen M. Thermal energy storage: systems and applications. Wiley; 2003.
- [37] Ministry of Land, Infrastructure, Transport and Tourism, ECLM tool ver.3.1. 2014.
- [38] The Society of Heating, Air-Conditioning and Sanitary Engineers of Japan (SHASE). Computer Aided Simulation for Cogeneration Assessment &amp; Design III, Maruzen Publishing, 2008.
- [40] The Society of Heating, Air-Conditioning and Sanitary Engineers of Japan (SHASE). NewHASP/ACl. Ver. 20091117, Japanese Association of Building Mechanical and Electrical Engineers, 2009.
- [41] TEPCO. Illustrated 2013-2013, TEPCO. 2013.
- [42] Takahashi T, Kawai K, Nakai H, Ema Y. Development of the automatic modeling of a system for reaction mechanisms using RX+G. Physics Procedia 2013:46:29-37.
- [43] Ono I, Kobayashi S, Yoshida K. Optimal lens design by real-coded genetic algorithms using UNG Comput Methods Appl Mech Eng 2008:164:483-97.
- [44] Van den Berg F, Enzlebrecht A. A study of particle swarm optimization, a particle trajectories. Inf. Sci. 2006:176:937-71.
- [45] Miranda V, Fonseca N. EP-ISO - Evolutionary Particle Swarm Optimization, a New Algorithm with Applications in Power Systems, Transmission and Distribution Conference and Exhibition 2002: Asia Pacific. IEEE/PES (Volume 2, 2002, p. 745-50).
- [46] Abou El Ala, Ağıdıo M, Seafi, Sr. Optimal power flow using differential evolution algorithm. Electric Power Syst Res 2010:80:878-85.
- [47] Mallipedi R, Jeyadevi S, Sungphanan P, Baskar S. Efficient constraint handling for optimal reactive power dispatch problems. Swarm Evol Comput 2012:5:28-36.
- [48] Karabóa K, Ódakem S. A simple and global optimization algorithm for engineering problems: differential evolution algorithm. Turk J Elect Eng 2004:12:1-53-60.
- [49] Yang S, X, Deb Sckoo. Research via Lévy Flights, Proc. of World Congress on Nature &amp; Biologically Inspired Computing (NAbic 2009). IEEE Publications, 2009. p. 210-14.
- [50] Ciugovici P, Besdako. A conceptual comparison of the Cuckoo-search, particle swarm optimization, a differential evolution and artificial bee colony algorithms. Artificial Intell Rev 2013:39:4-315-46.
- [51] Piechockj, J Ambrozki D, Palkowski A, Redlarski G. Use of Modified Cuckoo Search algorithm in the design process of integrated power systems for modern and energy self-sufficient farms. Appl Energy 2014:114:901-8.
- [52] Ahmed J, Salam Z. A maximum Point Power Tracking (MPMT) for PV system using Cuckoo Search with partial shading capability. Appl Energy 2014:119:18-30.

[53] Moravej Z, Akhlagi A. A novel approach based on cuckoo search for DG allocation in distribution network. Electrical Power Energy Syst 2014;44:672-9.

[54] Yang X. A new metaheutistic bat-inspired algorithm, nature inspired cooperative strategies for optimization (NISCO 2010). Stud Comput Intell 2010;284:65-74.

## Nomenclature

| acd †        | amount of charging/discharging of electricity at th ttime  interval (kW)                                    |
|--------------|-------------------------------------------------------------------------------------------------------------|
| acr †        | amount of storing/releasing of thermal energy at th ttime  interval (kW)                                    |
| c$_{1}$      | coefficient of returning to the past personal best pos- tion of PSO                                         |
| c$_{2}$      | coefficient of moving to the best position in all individ- uals of PSO                                      |
| c$_{b}$      | capacity of a battery (kW h)                                                                                |
| c$_{TES}$    | capacity of TES (kW h)                                                                                      |
| D$_{max}$    | maximum demand in all tim e horizons (kW)                                                                   |
| D$_{g}$      | electricity demand at th ttime interval (kW)                                                                |
| D$_{f}$      | cooling demand at th ttime interval (kW)                                                                    |
| e$_{C}$AHP   | electricity consumption for operating an AHP at th ttime  interval (kW)                                     |
| e$_{C}$Pump1 | electricity consumption for operating Pump 1 at th ttime  interval (kW)                                     |
| e$_{C}$Pump2 | electricity consumption for operating Pump 2 at th ttime  interval (kW)                                     |
| e$_{C}$eot   | electricity consumption for operating a battery and  meeting electricity demand at th ttime interval (kW)   |
| ef$_{b}$     | efficiency of charging/discharging of electricity ( - )                                                     |
| ef$_{s}$     | efficiency of storing/releasing of thermal energy ( - )                                                     |
| ep †         | price of electricity per kWh h ttime at th ttime (yen/ h)                                                   |
| ep$_{eof}$   | price of electricity for operating a battery and meeting  electricity demand at th ttime interval (yen/ h)  |
| ep$_{es}$    | price of electricity for operating an AHP and TES and  meeting cooling demand at th ttime interval (yen/ h) |
| f †          | frequency of th tl ln individual at th ttime interval                                                       |
| f min        | minimum value of frequency (0.0)                                                                            |
| f max        | maximum value of frequency ( - )                                                                            |
| loss$_{R}$S  | loss of energy of TES per an hour ( - )                                                                     |
| macd         | maximum amount of charging/discharging of electricity                                                       |
| macr †       | maximum amount of storing/releasing of thermal  energy at th ttime interval (kW)                            |

to solve a multi-objective problem of energy systems that include biomass energy. Fong et al. [7] applied a non-reversing strategy to a genetic algorithm (GA) and particle swarm optimization (PSO) to minimize life cycle costs in centralized air-conditioning systems. Lee and Kung [8] used PSO to minimize life cycle costs by optimizing the capacity and volume of melted ice of the ice in an air-conditioning system. Moradi et al. [9] applied a hybrid method combining PSO with fuzzy linear programming to optimize heat production and electricity dispatch of CHP. Wang et al. [10] used a GA to optimize the capacity and operation of combined cooling, heating, and power (CCHP) in comparison to a separation production system.

Although these previous studies provided effective optimization methods, they dealt with energy systems without storage equipment. On the other hand, the number of studies that have considered storage equipment has increased in recent years [11- 33]. Although there are many optimization methods, we can divide them into two categories, mathematical programming, such as MILP and dynamic programming (DP), and metaheuristic optimization or metaheuristics. MILP [11-20] and DP [21-23] are often used in previous studies, because those methods can always derive a theoretically optimal solution. However, their computation time is very long, when many decision variables and discrete points are included. In contrast, metaheuristics, such as neural networks [24],

max$\_{P}$AHP maximum power output of an AHP at th ttime interval (kW)

<!-- image -->

<!-- image -->

<!-- image -->

| Air-source heat  pump                                                                         | Cooling capacity (kW)                                                                         |   1000 |
|-----------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|--------|
| Thermal storage capacity (kW)                                                                 | 278.6                                                                                         | 3000   |
| Maximum permitted amount of  storing/releasing of thermal energy  during a time interval (kW) | Depending on  power output  from an AHP                                                       |    8   |
| Energy demand                                                                                 | Offering of storing/releasing  of thermal energy (-)                                          |    0.8 |
| Electric Battery capacity (kW h)                                                              | 0.002                                                                                         |  500   |
| Electric Battery capacity (kW h)                                                              | Maximum permitted amount of  charging/discharging of electricity  during a time interval (kW) |  100   |
| Electric Battery capacity (-)                                                                 | Offering of storing/releasing  of thermal energy (-)                                          |    0.9 |

intervals were 30 h and 1 h, respectively. A portion of the analyzed period overlaps with a portion of the warming-up period, because we can recalculate the operating schedule of overlapped time horizons, even if the schedule cannot be optimized sufficiently. Electricity demand representing electricity consumption by lighting and PCs was determined using Computer-Aided Simulation for Cogeneration Assessment &amp; Design III (CASCADE III), provided by the Society of Heating, Air-Conditioning and Sanitary Engineers of Japan (SHASE) [38]. Cooling demand was calculated using the New Heating, Air-conditioning, Sanitary Program/Airconditioning Conditioning (NewHASP/ACLD) [39]. Electricity demand, cooling demand, and outdoor temperature are shown in Fig. 4.

## 2.1.3. The price of electricity

The price of electricity in each time interval varies with the total hourly electricity consumption. In this paper, we considered the merit order as a price decision method of simulating an imaginary electricity market. Thus, we adopt four assumptions to obtain the price of electricity per kWh H: (1) the type of power plant, (2) the number of each type of power plant, (3) the composition rate of each power plant, and (4) the power generation costs of each type of power plant. First, the type of power plant was set to nuclear, liquid natural gas (LNG) fired, oil fired, coal fired, and hydroelectric, because those are the typical types. Second, the number of each type of power plant in the same order as mentioned above was set to 5, 16, 6, 10, and 8, respectively. The composition rate of each power plant was set to 27%, 40%, 17%, 2%, and 14%, respectively, as in [40]. It is important to consider the total capacity of all of the

<!-- image -->

plants in order to investigate a power shortage. Thus, we used Eq. (1) to obtain that total.

$$D _ { \max } = \max _ { a } \{ D _ { e } ^ { \prime } + D _ { e } ^ { \prime } \, \rho e ^ { \prime } \}$$

The assumed maximum electric consumption is 2226 kW at 8:00 a.m. in the warming-up period. Thus, the capacity of each type of power plant was set to 592.1, 899.3, 369.5, 55.7, and 309.4 kW, respectively. Finally, the power generation costs were taken from [41]. The merit order are shown in Fig. 5. In Fig. 4, 8:00 a.m., 1:00 p.m., and 2:00 p.m. in the warming-up period represent the peak times, because the price of electricity in the time intervals is 41.4 yen/kW h, the highest price, as shown in Fig. 5. The exchange rate of Japanese yen against US$ is 1 yen = $0.009.

## 2.2. Problem formulation

In this paper, the aim of the optimization is to minimize operating costs for 30 h in each calculation period, as follows:

Objective function:

$$\min _ { t = 1 } \frac { t i m e } { t = 1 } ( \exp e ^ { \epsilon _ { 0 } } + e p e s ^ { \epsilon } )$$

## Constraints:

$$0 \leqslant S _ { t } ^ { b } \leqslant C _ { b }$$

$$0 \leqslant a c d ^ { \prime } \leqslant m a c d$$

$$| a c d ^ { \prime } \cdot e f _ { 1 } | \leqslant D _ { e } ^ { \prime } ( a c d ^ { \prime } \leqslant 0 )$$

of thermal energy and the cooling demand, using Eqs. (23) and (24).

## 2.3. Methodology

## 2.3.1 DP

The computational accuracy of metaheuristics is difficult to determine, because the use of random numbers can prevent these methods from deriving the optimal solution. Thus, we estimated the accuracy of the metaheuristics in comparison with the optimal solution obtained by DP. We set discrete points to 1%. There are two calculation methods in DP, backward programming and forward programming. Backward programming determines optimal route, whereas forward programming determines optimal discrete points, as shown in Fig. 6.

## 2.3.2 GA

Although a GA generally involves binary variables, we applied a real-coded genetic algorithm (RCGA) with Real-coded Ensemble Crossover (REX) + Just Generation Gap (JGG) 42 to optimize continuous decision variables. RCGA with REX+JG is more efficient than RCGA with Unimodal Normal Distribution Crossover (UNDX) + Minimal Generation Gap (MGG), which was already known to be an efficient method [43]. In the RCGA with REX+JGG procedure, first, the population size is generally assigned to n (nc = 6nd ~ 22nd). Second, nd + k parents are selected randomly from the population of size n . Third, nc ~ 5nd ~ 10nd). Children are generated using the REX method with Eq. (25). Finally, nc -chillendren replace all selected parents. In this paper, we set k to 1.0 and nc to 6. No mutation method is required in RCGA with REX+JGG.

<!-- image -->

## 2.3.3 PSO

PSO, which imitates the collective behavior of birds and fish, is used frequently [7-9,26-31]. An individual of PSO has three types

<!-- image -->

of vector, the current velocity vector, the best position vector for all particles, and the past best position vector for itself, as shown in Fig. 7. Each individual moves to optimize the objective function by using Eq. (26).

$$\psi = \frac { v _ { i } ^ { 2 } } { w ^ { 2 } } + c _ { 1 } ^ { 1 } + c _ { 1 } ^ { 1 } ( x _ { p e b s t _ { i } } - \vec { x } _ { i } ) + c _ { 2 } r _ { 2 } ( x _ { b e s t _ { i } } ^ { 2 } - \vec { x } _ { i } ) \quad ( 2 6 )$$

PSO involves three parameters, w, c$\_{1}$, and c$\_{2}$, as shown in Eq. (26). Bergh and Engelbrecht [44] showed that PSO can have an advantage in finding the best solution, when Eq. (27) is specified.

$$\nu _ { i } ^ { 2 } \geq ( c _ { 1 } ^ { 2 } + c _ { 2 } ^ { 2 } ) - 1$$

In this paper, w = 0.7298 and c$\_{1}$ = c$\_{2}$ = 1.49618 were applied from [44]. Although PSO was reported as an efficient method in prior studies, it can become trapped in a local minimum of a multi-modal function. To improve the performance of PSO, Miranda [45] developed option-solved alpha-setting PSO (EPSO), which added an evolutionary method to classical PSO (c-PSO). In this paper, we develop PSO, which adds a mutation method to C-PSO, although both EPSO and m-PSO are improved in terms of evolution, they still differ. In EPSO, a mutation method with a Gaussian distribution was added to the velocity calculation in Eq. (26). In contrast, in PSO, we adopted a mutation method with uniformly distributed positions of individuals by Eq. (28).

$$X _ { i j } = \left \{ \begin{array} { c c } \mathcal { U } & \mathrm { f r a n d \, \mathrm { m r a t e } } \\ \mathrm { x _ { i j } } & \mathrm { f r a n d \, \mathrm { m r a t e } } \end{array} \right \}$$

(

where x$\_{i}$ j denotes each element of individual's vector, ˆ u ̂ = ⌊ Lb, Ub ⌋ denotes an uniformly distributed number that range is lower bound Lb and upper bound Ub of each decision variables. These values are in [ - 1 , 1] because all decision variables are normalized in [ - 1 , 1] in this paper. Thus, each element of an individual's vector is changed by r mate (mutation rate) with the specified probability after Eq. (26). We set it to 5%. Although m-PSO is a simpler improvement than EPSO, it showed a substantial advantage over both c-PSO and EPSO. In Section 3.3, the differences among c-PSO, EPSO, and m-PSO are discussed.

## 2.3.4 DE

- (1) Checking constraints, Eq. (6).
- If S$\_{F}$ 8 exceeds C$\_{b}$ , acd 8 is decreased to set S$\_{F}$ 8 equal to C$\_{b}$ , using Eq. (16). If S$\_{F}$ 8 is less than zero, acd 8 is revised to set S$\_{F}$ 8 equal to zero, using Eq. (17).
- (2) Checking constraints, Eq. (8).

If acd 8 in discharging mode is greater than D$\_{b}$ , acd 8 is set equal to the value of D$\_{b}$ , because the inability to sell electricity from the battery to the grid renders excessive discharging useless.

- (3) Checking constraints, Eq. (9) right side.

If S$\_{F}$ 8 exceeds C$\_{b}$ , acd 8 is decreased to set S$\_{F}$ 8 equal to C$\_{b}$ , using Eq. (19) and the power output of an AHP is also revised, using Eq. (23).

- (4) Checking constraints, Eq. (11) right side.

If P$\_{HP}$ 8 is greater than maxP$\_{HP}$ 8 , when TES is in the charging mode, acr 8 is decreased to set P$\_{HP}$ 8 equal to maxP$\_{HP}$ 8 . On the other hand, if P$\_{HP}$ 8 is greater than maxP$\_{HP}$ 8 , when TES is in the discharging mode, acr 8 , a negative number, must be increased to meet the cooling demand, because there is an energy shortage, even if an AHP generates maximum cooling thermal energy.

- (5) Checking constraints, Eq. (9) left side.

If S$\_{F}$ 8 is less than zero, acr 8 , a negative number, is decreased to set S$\_{F}$ 8 equal to zero, using Eq. (20) and P$\_{HP}$ 8 , is increased using Eq. (24), because the amount of discharging is reduced.

- (6) Checking constraints, Eq. (11) left side.

If P$\_{HP}$ 8 is negative, acr 8 , which is in discharging mode, is increased using Eq. (20), because acr 8 is greater than D$\_{c}$ .

- (7) Re-checking constraints, Eq. (11) right side.

We use a death penalty method when further change is needed in this phase.

Installing TES reduces the capacity of an AHP, which contributes to reducing energy consumption and costs. However, it causes an energy shortage, if there is insufficient energy stored in TES at peak time intervals. Further change indicates that there is an energy shortage in the time interval. We must revise the amount of charging in the in previous time interval to meet the cooling demand in the current interval. That indicates that high computation costs are required. Consequently, we use a death penalty method in the interval, when re-checking is required.

## 3. Results and discussion

## 3.1. The theoretically optimal solution

The theoretically optimal solution from DP is 305,335 yen/30 h in the analyzed period, and its computation time is 5 h, 1 min, 54 s. This value, 305,335 yen/30 h, is taken as the standard value, when the methaetureis are compared with DP.

## 3.2. Sensitivity analysis of the CS pa parameter

We conducted a sensitivity analysis of the CS parameter, pa, to determine suitable values for it. Although Yang and Deb [49] set pa to 0.25, they recommended using either 0.25 or 0.75, when applying CS to problems with small or huge domains [56], respectively. Then, five values were used with SC-II, 0.75, 0.8, 0.85, 0.9, and 0.95, with the results shown in Fig. 10. Although the minimum value when pa equals 0.85 is the smallest, a pa value of 0.9 is the most suitable in terms of average value and convergence. Consequently, we use a pa value of 0.9 after this section.

## 3.3. The advantage of m-PSO

The performance of m-PSO, EPSO, and m-PSO are shown in Fig. 11. Although adding a mutation method to c-PSO is simple, m-PSO is more accurate than c-PSO and EPSO. Therefore, mutation for an individual's position has an advantage in finding the optimal solution for our metaeurenistics.

## 3.4. Results of SC-I (Stopping criterion of tolerance)

The results of SC-I, which includes three kinds of tolerance criteria, are shown in Fig. 12: 0.1%, 0.5%, and 0.1%, m-PSO converges faster than the others, because m-PSO is the fastest with 1% and 0.5% tolerance. DE is the second fastest with 0.5% tolerance.

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->
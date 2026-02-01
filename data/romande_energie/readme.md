# Data sets made available by Romande Energie

## Rolle site ##

Data stored is stored at: `DEEP - TM - RG-AA - RG-AA\030 - Execution\ERA-NET AISOP\400 - Work Packages\Power flow forecaster\data` consisting of a sample of smart meter data and data from a power quality monitoring device (i.e., grid eye) in *feeder 13*  of Rolle Hospital site. 

## Other data files from KnowlEDGE ##

* `V2dataset_feeder_analysis/11_hourly_1week_anon_meters.csv`
* `V2dataset_feeder_analysis/12_mapping_feeder_information.csv`
* `V2dataset_feeder_analysis/20_hopital_anon_grid.json`
* `V2dataset_feeder_analysis/21_hopital_feeder13_anon_grid.json`

## Time series data from Romande Energie ##

we know: trafos and 3 cabinets
pache property: how is this connected to grid?

Data from Romande Energie shared at the end of 2023 consists of time series data from a site, a LV system *Champ Monnet*, located in the town of Chapelle-sur-Moudon. The data concerns two MV-LV transformers.
The data from each of the transformers is contained in two files one for the LV side and the other for the MV side. 

| id | file name | level | served by | Cyme_DeviceID | Cyme_NodeID |
| --- | --- | --- | --- | --- | --- |
Tr 7445 | `Transformateur Champ Monnet_BT.csv` | LV | Grid: Lucs | BIT 21/18 KV-CHAMP MONNET-7445 | 42883123 | 
Tr 7445 | `Transformateur Champ Monnet_MT.csv` | MV | Grid: Lucs | - | - |
Tr 3063 | `Transformateur Chapelle_BT.csv` | LV | Grid: Lucs | BIT 21/18 KV-CHAPELLE-3063¨ |  | 
Tr 3063 | `Transformateur Chapelle_MT.csv` | MV | Grid: Lucs | - | - |


The LV side are measurements of voltage and feed in current at the LV busbar, while the MW side values calculated from the LV measurement with Tr nameplate data.

1. Station **Champ Monnet** (transformer Tr 7445 in the XML grid dataset).
4 LV cabinets and multiple nodes. The data regarding the 4 LV cabinets is contained in 4 files as shown below.

| id | file name | description | served by 
| --- | --- | --- |
Tr 7445 | `Transformateur Champ Monnet_BT.csv` | Voltage and feed in current at the LV busbar | ?
Tr 7445 | `Transformateur Champ Monnet_MT.csv` | Values calculated from the LV measurement with Tr nameplate data | ?
? | `Battoir C6.csv` ?| Voltage of the cabinet busbar and current of the incoming line | Tr 7445
? | `Champ Monnet C4.csv` 102| Voltage of the cabinet busbar and current of the incoming line | Tr 7445
? | `MTE – CPM Champ Monnet.csv` is 104 connected here | Voltage of the cabinet busbar and current of the incoming line | Tr 7445
? | `Route de Villars Tiercelin C7.csv` ?| Voltage of the cabinet busbar and current of the incoming line | Tr 7445

**Notes**
- [ ] values from MV in Champ Monnet station (`Transformateur Champ Monnet_MT.csv`) are accurate up to August 19th 2022
- [ ] since Augutst 19th, 2022 the transformer has been changed by the operator for a 400 kVA instead of the former 250 kVA
- [ ] names of the cabinets should appear in your extraction in the chain substation-outgoing MV feeder-municipality code (here MTE)-distribution station-outgoing LV feeder- cabinet (but I’m not a user of our PSA Cyme – Ask Raphaël in case of doubt)

Data behind the meter from a customer served by this grid is also available.

2. Station **Chapelle** (transformer Tr 3063 in the XML grid dataset).
Voltage and feed in current at the LV busbar. Note that there is no connection between the LV systems of these two transformers – but you get an idee of the total consumption of the whole town.

Table of datasets:
| id | file name | description | served by 
| --- | --- | --- | --- |
Tr 3063 | `Transformateur Chapelle_BT.csv` | Voltage and feed in current at the LV busbar | ?
Tr 3063 | `Transformateur Chapelle_MT.csv` | Values Calculated from the LV measurement with Tr nameplate data | ?

3. **Customer** data (served by Tr 7445?). 
Behind the meter data is described below.

| id | file name | description | served by
|--- | --- | --- | --- | 
? | `Pache Home_Introduction.csv` | Description of the installation | Tr 7445
? | `Pache Home_PV installation.csv` | (72 kWp during the recording, soon 174 kWp) | Tr 7445
? | `Pache Home_Battery.csv` | (40 kWh/20 KVA) | Tr 7445

## Grid topology data from Romande Energie ##

Romande energie grid includes grid levels 4 to 7, that is HV-MV transformers, MV grid, MV-LV transformers, and the LV grid. 

Matpower grid topology data that were parse from CYME format to FlexDyn format are saved by ETH. Note that
1. bus ids are in sequential order starting from 1
2. **Cyme_NodeIDs** are save as **bus names** in the *mpc* struct
3. power flow was run successfully by ETH in using this matpower *mpc* struct file 

TODO: extract LV grids that serve TR7445 and TR3063




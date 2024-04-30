# Data sets made available by Romande Energie

## Rolle site ##
Data stored is stored at: `DEEP - TM - RG-AA - RG-AA\030 - Execution\ERA-NET AISOP\400 - Work Packages\Power flow forecaster\data` consisting of a sample of smart meter data and data from a power quality monitoring device (i.e., grid eye) in *feeder 13*  of Rolle Hospital site. 

## Other data files from KnowlEDGE ##
* `V2dataset_feeder_analysis/11_hourly_1week_anon_meters.csv`
* `V2dataset_feeder_analysis/12_mapping_feeder_information.csv`
* `V2dataset_feeder_analysis/20_hopital_anon_grid.json`
* `V2dataset_feeder_analysis/21_hopital_feeder13_anon_grid.json`

## Time series data from Romande Energie ##
Data from shared end of 2023 consists of time series data from a site, a LV system *Champ Monnet*, located in the town of Chapelle-sur-Moudon. The data concerns two MV-LV transformers.

1. Station **Champ Monnet** (transformer Tr 7445 in the XML grid dataset): 4 LV cabinets and multiple nodes. The data of the transformer is contained in two files one for the LV side and the other for the MV side. The data regarding the 4 LV cabinets is contained in 4 files. Data behind the meter from a customer served by this grid is also available.

Table of datasets:

file name | description
--- | ---
`Transformateur Champ Monnet_BT.csv` | Voltage and feed in current at the LV busbar
`Transformateur Champ Monnet_MT.csv` | Values calculated from the LV measurement with Tr nameplate data
`Battoir C6.csv` | Voltage of the cabinet busbar and current of the incoming line
`Champ Monnet C4.csv` | Voltage of the cabinet busbar and current of the incoming line
`MTE – CPM Champ Monnet.csv` | Voltage of the cabinet busbar and current of the incoming line
`Route de Villars Tiercelin C7.csv` | Voltage of the cabinet busbar and current of the incoming line

Note that the values from MV in Champ Monnet station (`Transformateur Champ Monnet_MT.csv`) are accurate up to August 19th 2022. Since the transformer has been changed by the operator for a 400 kVA instead of the former 250 kVA.

Note that the names of the cabinets should appear in your extraction in the chain substation-outgoing MV feeder-municipality code (here MTE)-distribution station-outgoing LV feeder- cabinet (but I’m not a user of our PSA Cyme – Ask Raphaël in case of doubt)


2. Station **Chapelle** (transformer Tr 3063 in the XML grid dataset): voltage and feed in current at the LV busbar. Note that there is no connection between the LV systems of these two transformers – but you get an idee of the total consumption of the whole town.

Table of datasets:
file name | description
--- | ---
`Transformateur Chapelle_BT.csv` | Voltage and feed in current at the LV busbar
`Transformateur Chapelle_MT.csv` | Values Calculated from the LV measurement with Tr nameplate data

3. **Customer** data served by Tr 7445. Behind the meter data is described ni the table below. These data is contained in three files described below.

file name | description
--- | ---
`Pache Home_Introduction.csv` | Description of the installation
`Pache Home_PV installation.csv` | (72 kWp during the recording, soon 174 kWp)
`Pache Home_Battery.csv` | (40 kWh/20 KVA)

## Grid topology data from Romande Energie ##ß
Romande energie grid includes grid levels 4 to 7, that is HV-MV transformers, MV grid, MV-LV transformers, and the LV grid. 

Matpower grid topology data that were parse from CYME format to FlexDyn format are saved by ETH. Note that
1. bus ids are in sequential order starting from 1
2. **Cyme_NodeIDs** are save as **bus names** in the *mpc* struct
3. power flow was run successfully by ETH in using this matpower *mpc* struct file 

TODO: extract LV grids that serve TR7445 and TR3063
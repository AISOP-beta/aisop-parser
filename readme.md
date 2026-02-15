# AISOP Parser

Data parsing, grid topology modeling, and visualization toolkit for the [ERA-NET AISOP](https://www.aramis.admin.ch/) project on power flow forecasting in low-voltage distribution grids.

## Overview

This repository provides tools to:

- **Parse** measurement data from GridEye power quality monitoring devices
- **Model** MV/LV distribution grid topologies from MATPOWER case files
- **Run** power flow simulations via GridCalEngine and pandapower
- **Visualize** grid networks on interactive maps (Folium/Plotly) and plot time series
- **Integrate** meteorological data from multiple providers (MeteoSwiss, DWD, Open-Meteo, NREL, etc.)

The primary dataset comes from the Romande Energie distribution network in the Chapelle-sur-Moudon region (Switzerland), covering two MV/LV transformers, four LV distribution cabinets, and behind-the-meter prosumer installations.

## Project structure

```
parser/src/          Source modules
  parser.py          GridEye CSV data parser (extends pd.DataFrame)
  topology.py        Grid topology parsing and power flow setup
  viz.py             Network visualization on maps (Folium, Plotly)
  plotter.py         Time series and statistical plotting
  re.py              Regex utilities for GridEye column headers
  read_writeS3.py    S3 / SWITCH object storage interface
examples/            Usage examples (Chapelle analysis, data ingestion, Prefect flows)
data/
  romande_energie/   GridEye measurements, grid topology (.m files), metadata
  enduser/           Behind-the-meter customer data and tariffs
  meteo/             Weather data (DWD, IDAWEB, Open-Meteo, Meteostat, NREL, etc.)
  plots/             Generated figures
```

## Key dependencies

| Category | Libraries |
|---|---|
| Data | pandas, numpy, polars, pyarrow, fastparquet |
| Power systems | pandapower, GridCalEngine, pvlib, windpowerlib |
| Visualization | matplotlib, seaborn, plotly, folium |
| Geospatial | pyproj, geopy, networkx |
| Optimization | or-tools, pymoo, cma, highspy |
| ML / Stats | scikit-learn, scipy |

See `requirements.txt` for the full list.

## Installation

```bash
pip install -r requirements.txt
```

## Data sources

### Romande Energie grid measurements

Measurements from GridEye sensors on the LUCS grid:

- **TR 7445** (Champ Monnet) -- transformer LV/MV sides + 4 LV cabinets (Battoir C6, Champ Monnet C4, MTE, Route de Villars Tiercelin C7)
- **TR 3063** (Chapelle) -- transformer LV/MV sides
- **Pache Home** -- prosumer with PV (72-174 kWp) and battery (40 kWh / 20 kVA)

### Grid topology

MATPOWER case files (`.m`) converted from CYME/XML via FlexDyn, covering HV-MV-LV network layers 4-7.

### Meteorological data

Multiple providers under `data/meteo/`: DWD, MeteoSwiss IDAWEB, Open-Meteo, Meteostat, Meteomatics, MeteoBlue, NREL.

## Object storage

AISOP public object storage on SWITCH Ceph gateway:

```python
_endpointS3 = "https://s3-zh.os.switch.ch/"
_endpoint   = "https://os.zhdk.cloud.switch.ch/"
```

Public bucket: `https://os.zhdk.cloud.switch.ch/swift/v1/aisop_public/`

Reference: [SWITCH Object Storage docs](https://help.switch.ch/engines/documentation/object-storage/s3-clients-and-libraries/)
# 🚗⚡ Electric vehicle Adoption vs Clean Electricity  

## Description  
This project explores the relationship between **electric vehicle (EV) adoption** (measured by cars sold annually) and the **cleanliness of national electricity systems** (measured as share of electricity from low-carbon sources).  

The visualization combines a **Leaflet map** (for spatial distribution) and a **D3 scatter plot** (for statistical relationship) to investigate whether cleaner electricity grids are associated with higher EV adoption.  

**Hypothesis:** Countries with cleaner electricity (higher share of renewables/nuclear, lower fossil fuel use) tend to adopt EVs more rapidly.  

---

## Setup Instructions  
1. Download and extract all project files.  
2. Run the visualization in one of the following ways:  
   - Open `index.html` directly in a modern browser. 
   - Or serve via a local server (recommended for avoiding CORS issues when loading local GeoJSON/CSV files):  
     - **VS Code**: Use the *Live Server* extension.
     - **Python 3**: Run `python -m http.server 8000` and open `http://localhost:8000`.  

### CORS Considerations  
- Some browsers block local file access (`file://`) for JSON/CSV.  
- Using a local server is the most reliable method to ensure datasets load properly.  

---

## File Structure  

### Main Deliverable
- **`index.html`** – Final main visualization page, includes map + scatter plot.

### Supporting Tasks

- **`task5_6/`**  
  - `main.py` – Initial script to merge `ev_sales.csv` + `energy_emissions.csv`.  
  - `merged_data.csv` – Output dataset from preprocessing.  
  - `task5.html` – Exploratory Data Analysis (distributions, time series, scatter plots).  
  - `task6.html` – Visualization type evaluation with D3.js & Leaflet mockups.  

- `task7_8.html` – Data preprocessing and dataset joining: Produces `master_data.geojson`.  

- `task9.html` – Statistical analysis
    
- **`/data/`**
  - `ev_sales.csv` – Annual number of new electric cars sold (per country, per year).  
  - `energy_emissions.csv` – Energy mix and emissions intensity (per country, per year).   
  - `master_data.geojson` – Primary merged dataset combining EV sales and clean electricity share.  
  - `master_data_backup.geojson` – Backup dataset in case the primary file fails to load.    

---

## Usage  
- **Dropdown Filters**:  
  - *Year Selector* – View EV adoption for a specific year or all years.  
  - *Region Selector* – Filter by world region.  
- **Map (Leaflet + Marker Clusters):**  
  - Bubble size = EV sales.  
  - Bubble color = Clean electricity share.  
  - Click a cluster to expand into individual countries.  
  - Click a country to see all the markers for different years.
  - Click a marker to view popup. 
- **Scatter Plot (D3):**  
  - X-axis = Clean electricity share (%).  
  - Y-axis = EV sales.  
  - Circle size = EV sales.  
  - Circle color = Clean electricity share.  
  - Hover to see country details.  
  - Brush a region to highlight corresponding map markers.  
  - Zoom & pan with mouse wheel or drag.  
- **Legends**:  
  - Both map and chart include color and size legends for interpretation.  

---

## Data Sources  
- **Electric Vehicle Sales Data**:  
  - *Number of New Electric Cars Sold*
  - International Energy Agency. Global EV Outlook 2025. – processed by Our World in Data  
  - [OWID Dataset Link](https://ourworldindata.org/grapher/electric-car-sales) 
  - [License: CC-BY](https://creativecommons.org/licenses/by/4.0/) 

- **Clean Electricity Data**:  
  - *World energy data 1990 - 2020*
  - [Kaggle Dataset Link](https://www.kaggle.com/datasets/shub218/energy-data-1990-2020)  
  - [License: World Bank Dataset Terms of Use](https://www.worldbank.org/en/about/legal/terms-of-use-for-datasets)  

---

## Known Issues & Limitations  
- Some countries/years are missing due to gaps in datasets.  
- EV adoption data varies in reporting accuracy between countries.

---

## Author

Developed by: Ayesha A. Jan  
Email: Ayesha.Jan@stud.srh-campus-berlin.de  
🎓 BST Data Visualizations – 2025

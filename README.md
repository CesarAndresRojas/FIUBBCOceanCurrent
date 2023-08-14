# BBCOceanCurrent
This code was developed during my time as a NASA Intern during the Summer 2023 semester.

## Prerequisites

- Python 3.x installed on your system
- Required Python packages (Install with `pip install -r requirements.txt`): matplotlib,scikit-learn,shapely,numpy,pandas,cartopy,GDAL

## Note for Windows users:
Installing GDAL and Cartopy packages on Windows is complicated, for higher chances of success please do the following:

1. Download and install Visual C++ Build Tools: https://visualstudio.microsoft.com/visual-cpp-build-tools/
   
3. Download precompiled GDAL Wheel: https://www.lfd.uci.edu/~gohlke/pythonlibs/#gdal
   
5. Install GDAL wheel with PIP: `pip install package-name.whl`
   
7. Install Cartopy from github with PIP: `pip install git+https://github.com/SciTools/cartopy`


## Getting Started

1. Clone this repository to your local machine.

2. Install the required Python packages by running `pip install -r requirements.txt`.

3. 'plot_oscar.py' plots ocean current speed and direction from oscar data_set

4. 'plot_oscar_region.py' does the same but zooms in to a region as per a geojson file.

5. 'plot_oscar_region_satellite.py' does the same but includes google earth imagery.

6. 'plot_tcm1_region_satellite.py' plots a single data point collected via TCM-1 tilt current meter.

## Usage

Both scripts do the following:

- Reads datasets in the 'in' directory

- Plots ocean current data from remote and in-situ sensing.

- Outputs Charts to the 'out' directory

## Contributors

- Cesar A. Rojas(https://github.com/croja022)

## Related Links
- NASA OSCAR Dataset(https://podaac.jpl.nasa.gov/dataset/OSCAR_L4_OC_third-deg#)

## License

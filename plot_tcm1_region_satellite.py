import pandas as pd
import json
import numpy as np
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import cartopy.io.img_tiles as cimgt
import matplotlib.pyplot as plt
from shapely.geometry import Polygon

# Load the GeoJSON file and extract the region coordinates
region_path = "input/Biscayne_Bay_Campus_Pier_Square.json"  # Replace with the path to your GeoJSON file

# Load the CSV files
speed_data = pd.read_csv('input/2008025_TCM08__(0)_Current.csv', parse_dates=['ISO 8601 Time'])
gps_data = pd.read_csv('input/2008025_TCM08__(0)_GPS.csv', parse_dates=['ISO 8601 Time'])

# Choose the desired record index (e.g., 3rd record)
selected_index = 3

# Extract data for the selected record
speed_record = speed_data.iloc[selected_index]
gps_record = gps_data.iloc[selected_index]

# Extract information from the selected records
speed = speed_record['Speed (cm/s)']
heading = np.radians(speed_record['Heading (degrees)'])
latitude = gps_record['Latitude']
longitude = gps_record['Longitude']

with open(region_path, "r") as f:
    geojson = json.load(f)
region_geometry = geojson["features"][0]["geometry"]

# Extract the region coordinates from the GeoJSON file
region_coordinates = region_geometry["coordinates"][0]

# Determine the minimum and maximum latitude and longitude values
lon_min, lat_min = np.min(region_coordinates, axis=0)
lon_max, lat_max = np.max(region_coordinates, axis=0)

# Set up the Cartopy map with Google Tiles satellite imagery
ax = plt.axes(projection=ccrs.PlateCarree())

# Define the tile source using a web map tile service (WMTS)
request = cimgt.GoogleTiles(style='satellite')
ax.add_image(request, 20)  # You can adjust the zoom level (e.g., 14) to change the level of detail

# Plot the ocean current arrow
arrow_dx = np.sin(heading) * speed
arrow_dy = np.cos(heading) * speed
ax.quiver(longitude, latitude, arrow_dx, arrow_dy, color='blue', scale=50, width=0.005, transform=ccrs.PlateCarree())

# Add coastlines and gridlines
ax.coastlines()
ax.gridlines(draw_labels=True)

# Set the region extent
extent = [lon_min, lon_max, lat_min, lat_max]
ax.set_extent(extent, crs=ccrs.PlateCarree())

# Add a colorbar with a label
sm = plt.cm.ScalarMappable(cmap='viridis', norm=plt.Normalize(vmin=speed_data['Speed (cm/s)'].min(), vmax=speed_data['Speed (cm/s)'].max()))
sm._A = []  # Hack to create a mappable without a mappable
cbar = plt.colorbar(sm, ax=ax, orientation='vertical')
cbar.set_label('Ocean Current Speed (cm/s)')

# Set the title of the plot
plt.title('Ocean Current Analysis')

plt.show()
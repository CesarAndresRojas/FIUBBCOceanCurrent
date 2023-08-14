import xarray as xr
import json
import numpy as np
import cartopy
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import cartopy.io.img_tiles as cimgt
import matplotlib.pyplot as plt
from shapely.geometry import Polygon

# Load the GeoJSON file and extract the region coordinates
region_path = "input/Biscayne_Bay_Campus_Pier_Square.json"  # Replace with the path to your GeoJSON file

with open(region_path, "r") as f:
    geojson = json.load(f)
region_geometry = geojson["features"][0]["geometry"]

# Extract the region coordinates from the GeoJSON file
region_coordinates = region_geometry["coordinates"][0]

# Determine the minimum and maximum latitude and longitude values
lon_min, lat_min = np.min(region_coordinates, axis=0)
lon_max, lat_max = np.max(region_coordinates, axis=0)

print(lon_min)
print(lat_min)
print(lon_max)
print(lat_max)

# Load the netCDF file
image_path = 'input/oscar_vel11237.nc'

with xr.open_dataset(image_path) as ds:
    print(ds)

    ax = plt.axes(projection=ccrs.PlateCarree())

    # Define the tile source using a web map tile service (WMTS)
    request = cimgt.GoogleTiles(style='satellite')
    ax.add_image(request, 20)  # You can adjust the zoom level (e.g., 14) to change the level of detail

    # Set the region extent
    extent = [lon_min, lon_max, lat_min, lat_max]

    # Limit the plot to the desired region
    ax.set_extent(extent, crs=ccrs.PlateCarree())

    # Determine the density of streamlines
    density = 2  # You can adjust this value as needed to get more or fewer lines

    # Plot the ocean current vectors within the region
    dec = 10
    lon = ds.longitude.values[::dec]
    lon[lon > 180] = lon[lon > 180] - 360
    # Calculate the speed (magnitude) of the ocean current vectors
    speed = np.sqrt(ds.u.values[0, 0, ::dec, ::dec]**2 + ds.v.values[0, 0, ::dec, ::dec]**2)

    mymap = plt.streamplot(lon, ds.latitude.values[::dec], ds.u.values[0, 0, ::dec, ::dec], ds.v.values[0, 0, ::dec, ::dec],
                           color=speed, cmap='viridis', linewidth=2, transform=ccrs.PlateCarree(), density=density)

    # Add map features (e.g., coastline, gridlines, etc.)
    ax.coastlines()
    ax.gridlines(draw_labels=True)

    # Create a Polygon from the region coordinates
    region_polygon = Polygon(region_coordinates)

    # Plot the region boundary from the Polygon
    ax.add_geometries([region_polygon], ccrs.PlateCarree(), facecolor='none', edgecolor='red')

    # Add a colorbar with a label
    cbar = plt.colorbar(mymap.lines)
    cbar.set_label('Ocean Current Speed (m/s)')

    # Set the title of the plot to be the filename
    plt.title(f'Ocean Current Analysis: {image_path}')
    plt.show()

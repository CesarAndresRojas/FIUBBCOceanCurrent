import xarray as xr
import json
import numpy as np
import cartopy
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.pyplot as plt
from shapely.geometry import Polygon
from cartopy.io import shapereader
from cartopy.mpl.patch import geos_to_path

# Load the netCDF file
image_path = 'input/oscar_vel11237.nc'

with xr.open_dataset(image_path) as ds:
    print(ds)

    ax = plt.axes(projection=ccrs.PlateCarree())

    ax.stock_img()
    ax.add_feature(cartopy.feature.LAND)
    ax.add_feature(cartopy.feature.OCEAN)
    ax.add_feature(cartopy.feature.COASTLINE)
    ax.add_feature(cartopy.feature.BORDERS, linestyle='-', alpha=.5)

    dec = 10
    lon = ds.longitude.values[::dec]
    lon[lon>180] = lon[lon>180] - 360
    mymap=plt.streamplot(lon, ds.latitude.values[::dec], ds.u.values[0, 0, ::dec, ::dec], ds.v.values[0, 0, ::dec, ::dec], 6, transform=ccrs.PlateCarree())
    ax.coastlines()
    plt.show()

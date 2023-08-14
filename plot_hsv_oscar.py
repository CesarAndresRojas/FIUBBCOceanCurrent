import xarray as xr
import numpy as np
import matplotlib.pyplot as plt

# Load the netCDF file
image_path = 'input/oscar_vel11237.nc'

with xr.open_dataset(image_path) as ds:
    U = ds['u'].values[0, 0, :, :]  # Extract U component
    V = ds['v'].values[0, 0, :, :]  # Extract V component

    # Calculate the magnitude of currents
    magnitude = np.sqrt(U**2 + V**2)

    # Normalize the magnitude to [0, 1]
    magnitude_norm = (magnitude - np.min(magnitude)) / (np.max(magnitude) - np.min(magnitude))

    # Create HSV plot
    plt.imshow(np.dstack((np.arctan2(V, U), np.ones(U.shape), magnitude_norm)), origin='lower')
    plt.colorbar(label='Magnitude')
    plt.title('HSV Plot of Ocean Currents')
    plt.show()

""" 

This script calculates wind speeds and directions from ERA5 (met convention) u and v wind components.

It also plots a wind rose of the results.  Place windrose.py also in the same folder where you are running this script.

Becca Rolph rebecca.rolph@nrel.gov
18 May 2022

"""

import numpy as np
import matplotlib.pyplot as plt
import xarray as xr
from os.path import exists
from windrose import WindroseAxes


convert_to_nc = False# 
# Specify site/filename to create windrose from
sitename = 'Kitty_hawk_a'
lat = 36.06918
lon = -75.1064  

wind_data_ifile_grb = 'data/grbfiles/' + sitename + '.grib'
wind_data_ifile_nc = 'data/ncfiles/' + sitename + '.nc'

if exists(wind_data_ifile_nc) == False:
    # Convert grb to ncfile
    wind_data_ifile_grb.to_netcdf()

# Read dataset
ds = xr.open_dataset(wind_data_ifile_nc)

# Find lat/lon that is contained in the ncfile which is closest to the input lat/lon
def geo_idx(dd, dd_array):
   """
     search for nearest decimal degree in an array of decimal degrees and return the index.
     np.argmin returns the indices of minium value along an axis.
     so subtract dd from all values in dd_array, take absolute value and find index of minium.
    """
   geo_idx = (np.abs(dd_array - dd)).argmin()
   return geo_idx

lat_in_file = geo_idx(lat, ds.latitude.values)
lon_in_file = geo_idx(lon, ds.longitude.values)

# Extract wind speed and direction from ifile, using data closest to the input lat/lon 
u100 = ds['u100'].isel(longitude=lon_in_file, latitude=lat_in_file)
v100 = ds['v100'].isel(longitude=lon_in_file, latitude=lat_in_file)

wind_speed = np.sqrt(u100**2 + v100**2) # [m/s]

def wind_uv_to_dir(U,V):
    """
    Calculates the wind direction from the u and v component of wind.
    Takes into account the wind direction coordinates is different than the 
    trig unit circle coordinate. If the wind directin is 360 then returns zero
    (by %360)
    Inputs:
      U = west/east direction (wind from the west is positive, from the east is negative)
      V = south/noth direction (wind from the south is positive, from the north is negative)
    """
    WDIR= (270-np.rad2deg(np.arctan2(V,U)))%360
    return WDIR

wind_dir = wind_uv_to_dir(u100, v100)

wind_speed_bins = np.histogram(wind_speed, 5)[1]

fig = plt.figure()
ax1 = fig.add_subplot(111, projection='windrose')
ax1.bar(wind_dir, wind_speed, normed=True, opening=0.8, edgecolor='white', bins=wind_speed_bins)
ax1.set_title(sitename)

ax1.legend(bbox_to_anchor=(1.2 , -0.1))
plt.tight_layout()
plt.show()

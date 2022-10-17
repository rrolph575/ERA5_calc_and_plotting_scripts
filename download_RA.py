# -*- coding: utf-8 -*-

""" This script downloads 100m u and v wind components from ERA5 nearby a specific point. It can be modified as necessary for 
different variables and time frames. To get the required packages this script needs to run, see the Climate Data Store at 
https://cds.climate.copernicus.eu/api-how-to

Becca Rolph rebecca.rolph@nrel.gov
18 May 2022

"""

import cdsapi
import numpy as np
import pandas as pd
from datetime import time


# Specify sitename and its lat/lon

#sitename = 'Kitty_hawk_a'
#lat = 36.06918
#lon = -75.1064  

#sitename = 'Empire_wind'
#lat = 40.40
#lon = -73.52

#sitename = 'CVOW_Commercial_a'
#lat = 36.80
#lon = -75.37

#sitename = 'Mayflower'
#lat = 40.78
#lon = -70.69

sitename = 'Carolina_Long_Bay'
lat = 33.6
lon = -78.3

# Specify the years you want the data extracted
year_start = 2018 
year_end =  2021 # Inclusive

# Specify months
month_start = 1
month_end = 12 # Inclusive

c = cdsapi.Client()

def download_ERA5(year_start, year_end, month_start, month_end, sitename, lat, lon):
    
    # Convert inputs into the format needed for cdsapi
    years = np.arange(year_start, year_end+1)
    years_str = ['{0}'.format(year) for year in years]
    months = np.arange(month_start,month_end+1)
    months_str = ['{0}'.format(month).zfill(2) for month in months]
    days = np.arange(1,32)
    days_str = ['{0}'.format(day).zfill(2) for day in days]
    date_range = pd.date_range('00:00', '23:00', freq='h')
    hours_str = date_range.strftime("%H:%M:%S").to_list()
    
    ERA5_grid_resolution = 0.25 # degrees
    north_lat = lat + ERA5_grid_resolution/2
    south_lat = lat - ERA5_grid_resolution/2
    west_lon = lon - ERA5_grid_resolution/2
    east_lon = lon + ERA5_grid_resolution/2
    
    grb_out_filename = 'data/grbfiles/' + sitename + '.grib'
    
    # Call cdsapi
    c.retrieve(
        'reanalysis-era5-single-levels',
        {
             'product_type': 'reanalysis',
             'format': 'grib',
             'variable': [
                 '10m_u_component_of_wind',
                 '10m_v_component_of_wind',
                 'significant_height_of_combined_wind_waves_and_swell',
              ],
             'year': years_str,
             'month': months_str,
             'day': days_str,
             'time': hours_str,
             'area': [
                 north_lat, west_lon, south_lat, east_lon],
        },
        grb_out_filename)

    return 'ERA5 data is now saved in ' + grb_out_filename

download_ERA5(year_start, year_end, month_start, month_end, sitename, lat, lon)

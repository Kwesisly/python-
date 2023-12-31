# -*- coding: utf-8 -*-
"""Copy of Copy of Attachment_1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1iDCutUPfo7Bddv-ZLyw2g0phqYSp9_Oe
"""

met253.2023@gmail.com

### using the link below. Download the data attached.

"""Using the link below. Download the data and upload it in your coolab repository.
https://drive.google.com/file/d/1MNebCCSclqHj09ijz8lDN4jJqFCh5Vmq/view?usp=drive_link
"""

!pip install -q condacolab

import condacolab

condacolab.install()

import cartopy

!mamba install -q -c conda-forge cartopy

import xarray as xr
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cartopy as cp
import cartopy.crs as ccrs
import cartopy.feature as cf
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter
from pathlib import Path
import warnings
warnings.filterwarnings('ignore')

dat = pd.read_fwf('/content/GMet_location_avgSI.txt', names = ['Station', 'Longitude', 'Latitude', 'St'])
dat

#####################  Plot for  study Area #######

plt.figure(figsize=(10,9))                         ###### Specifying the size of the figure
ax = plt.axes(projection = ccrs.PlateCarree())       ###### Specifying the type of geopatial plot
ax.add_feature(cf.COASTLINE,alpha=0.8)
ax.add_feature(cf.BORDERS)
ax.add_feature(cf.LAND)
ax.add_feature(cf.LAKES)
ax.add_feature(cf.OCEAN)
ax.add_feature(cf.RIVERS)
ax.stock_img()
ax.set_extent([-3.5,1.2,11.4,4.5])                   #### setting the map boundaries

ax.add_feature(cf.STATES, alpha= 0.1)               ####  adding territorial boundaries

ax.plot(dat.Longitude,
        dat.Latitude,
        'ro',                                       ##### plotting the longitudes and latitudes of the station
        ms=7,
        color = 'k')


s_stations = np.asarray(dat.Station)


for longitude, latitude, name in zip(dat.Longitude, dat.Latitude, s_stations):
    if name in ['Yendi']:
        ax.text(longitude - .03, latitude - .15,
                name,
                va='center',
                ha='center', transform=ccrs.Geodetic(), fontweight='bold',fontsize = '10')
    elif name in ['Zuarungu']:
        ax.text(longitude + .05, latitude - .20,
                name,
                va='center',
                ha='center', transform=ccrs.Geodetic(), fontweight='bold',fontsize='10')
    elif name in ['Takoradi']:
        ax.text(longitude + .05, latitude - .20,
                name,
                va='center',
                ha='center', transform=ccrs.Geodetic(), fontweight='bold',fontsize='10')
    elif name in ['Accra']:
        ax.text(longitude + .05, latitude - .15,
                name,
                va='center',
                ha='center', transform=ccrs.Geodetic(), fontweight='bold',fontsize='10')
    elif name in ['Akatsi']:
        ax.text(longitude - .05, latitude + .15,
                name,
                va='center',
                ha='center', transform=ccrs.Geodetic(), fontweight='bold',fontsize='10')
    elif name in ['Akuse']:
        ax.text(longitude - .05, latitude - .15,
                name,
                va='center',
                ha='center', transform=ccrs.Geodetic(), fontweight='bold',fontsize='10')
    else:
        ax.text(longitude + .09, latitude + .12,
                name,
                va='center',
                ha='center', transform=ccrs.Geodetic(), fontweight='bold',fontsize = '10')

ax.set_xticks([-3.2,-2.2,-1.2,0,1.2], crs=ccrs.PlateCarree())
ax.set_yticks([11,10,9,8,7,6,5], crs=ccrs.PlateCarree())
lon_formatter = LongitudeFormatter(zero_direction_label=True)
lat_formatter = LatitudeFormatter()
ax.xaxis.set_major_formatter(lon_formatter)
ax.yaxis.set_major_formatter(lat_formatter)
#long x lat y












---
title: Carbon.bird
emoji: 💻
colorFrom: yellow
colorTo: blue
sdk: gradio
sdk_version: 3.20.1
app_file: app.py
pinned: false
license: apache-2.0
---

Clim4x is a climate AI project, developing enhanced climate projections
by correcting using observerational data.

https://docs.google.com/document/d/1mZgRFhKuqv9cWR1RvxGKw20VoKU6Qwc9dB62n636PYE/edit

air temp from satellite land temp
https://www.nature.com/articles/sdata2018246


Data Sources:

NCAR
https://rda.ucar.edu/thredds/catalog/catalog.html

NOAA
https://www.ncei.noaa.gov/thredds/catalog.html

NASA
https://data.giss.nasa.gov/gistemp/

Gistemp also available on opendap
gistemp/combined/250km/
           air.2x2.250.mon.1991-2020.ltm.comb.nc
           air.2x2.250.mon.anom.comb.nc

Xarray can be fast or slow, depending. Think carefully about what your function calls
are triggering.
https://climate-cms.org/posts/2021-07-29-coarsen_climatology.html

Converting to/from xarray and panads: 
xarray: dataarrays, dataframes and 
pandas: multi-indexes panesl deprecated
https://docs.xarray.dev/en/stable/user-guide/pandas.html


Using netCDF4 files in Python:
https://pypi.org/project/netCDF4/

Plotting
Use html renderer for ease
https://plotly.com/python/renderers/
Combine map and contour
https://gradio.app/plot-component-for-maps/
https://plotly.com/python/contour-plots/
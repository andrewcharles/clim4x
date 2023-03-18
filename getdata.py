import xarray as xr
import os.path

def get_dap(url="url"):
    """ Get data from the NCAR research data archive """
    try:
        dataset =xr.open_dataset(url)
        return(dataset)
    except Exception as e:
        print(f"error {e}")

clim_url = "http://psl.noaa.gov/thredds/dodsC/Datasets/gistemp/combined/250km/air.2x2.250.mon.1991-2020.ltm.comb.nc"
data_url = "http://psl.noaa.gov/thredds/dodsC/Datasets/gistemp/combined/250km/air.2x2.250.mon.anom.comb.nc"

cds = get_dap(url=clim_url)
ds = get_dap(url=data_url)

# get the major variable names
print(list(ds))
vnam = "air"
data_dir = "data"

cds.to_netcdf(os.path.join(data_dir,"gistemp_clim_1991-2020.nc"))
ds.to_netcdf(os.path.join(data_dir,"gistemp.nc"))

#from pydap.client import open_url

import netCDF4

def get_dap(url="url"):
    """ Get data from the NCAR research data archive """
    try:
        dataset = netCDF4.Dataset(url)
        return(dataset)
    except Exception as e:
        print(f"error {e}")

get_dap(url="http://psl.noaa.gov/thredds/dodsC/Datasets/gistemp/combined/250km/air.2x2.250.mon.1991-2020.ltm.comb.nc")


def get_rda():
    """ Get data from the NCAR research data archive """
    try:
        url = "https://rda.ucar.edu/thredds/dodsC/files/g/ds094.2/regular/pgbl.gdas.202302.tar"
        dataset = netCDF4.Dataset(url)
        print(dataset)
    except Exception as e:
        print(f"error {e}")


#url = 'http://dtvirt5.deltares.nl:8080/thredds/dodsC/opendap/rijkswaterstaat/jarkus/profiles/transect.nc'
#url = "https://www.ncei.noaa.gov/thredds/dodsC/noaa-global-temp-v5.1/NOAAGlobalTemp_v5.1.0_gridded_s185001_e202301_c20230208T152556.nc"
#url = "https://www.ncei.noaa.gov/thredds/dodsC/sat/landcover/HH_AREAVEG/land-cover_hh_landcover_yr1770.nc"
#dataset = netCDF4.Dataset(url)
#remote_data = xr.open_dataset(
#remote_data = netCDF4.Dataset(
#    "http://iridl.ldeo.columbia.edu/SOURCES/.OSU/.PRISM/.monthly/dods",
#)
#print(remote_data)
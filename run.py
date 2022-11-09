import urllib.request

import rasterio


urllib.request.urlretrieve(
    "http://fatra.cnr.ncsu.edu/us-iale2017/US_elevation.tif", "elevation.tif"
)

with rasterio.open("elevation.tif") as dem:
    print(dem.crs)

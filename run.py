import rasterio

with rasterio.open("http://fatra.cnr.ncsu.edu/us-iale2017/US_elevation.tif") as dem:
    print(dem.crs)

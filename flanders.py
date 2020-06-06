import os
import geopandas as gpd
import matplotlib.pyplot as plt

# Set data directory
# Data origin: https://old.atlas-belgique.be/cms2/index.php?page=cartodata_fr
cwd = os.getcwd()
fp = os.path.join(cwd, 'Regions_08', 'régions_08.shp')

# Read shapefile
shp = gpd.read_file(fp)
print(shp.head())
# Map projection: Lambert 2008 (EPSG:3812) | WGS84 (EPSG:4326)
print(shp.crs)

# Extract Flanders
flanders = shp[shp['Nom'].isin(['Vlaams Gewest'])]
flanders.plot()
plt.show()

# Re-Projecting | Re-projecting is the process of changing the representation of locations from one coordinate system
# to another. All projections of locations on the Earth into a two-dimensional plane are distortions, the projection
# that is best for your application may be different from the projection associated with the data you import. In
# these cases, data can be re-projected using the GeoDataFrame.to_crs() command:

flanders_wgs = flanders.to_crs("EPSG:4326")
flanders_wgs.plot()
plt.show()






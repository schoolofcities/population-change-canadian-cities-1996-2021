import pandas as pd
import geopandas as gpd
from shapely.geometry import Point

df = pd.read_csv("data21.csv")

gdf = gpd.read_file("data/ct/ct_2021_wgs84.geojson")

gdf.geometry = gdf.geometry.representative_point()

gdf = gdf.merge(df, left_on='CTUID', right_on='ctuid')

gdf = gdf[["ctuid","pop96","pop21","geometry","LANDAREA"]]

gdf.to_file("ct_centroids.geojson")

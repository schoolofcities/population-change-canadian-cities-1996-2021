import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
import random

df = pd.read_csv("data21.csv")

gdf = gpd.read_file("data/ct/ct_2021_wgs84.geojson")

df["dif"] = df["pop21"] - df["pop96"]
df["dots"] = df["dif"] / 100
df["dots"] = df["dots"].astype(int)

print(df)

def gen_dot(ctuid, number):

    ct = gdf.loc[gdf["CTUID"] == ctuid]

    polygon = ct.geometry

    points = []
    
    while len(points) < number:
        pnt = Point(random.uniform(polygon.bounds.minx, polygon.bounds.maxx), random.uniform(polygon.bounds.miny, polygon.bounds.maxy))
        if polygon.iloc[0].contains(pnt):
            points.append([pnt.x,pnt.y])
    return points

    

    



all_dots = []

for i, row in df.iterrows():

    if row["dots"] > 0:

        dots = gen_dot(row["ctuid"], row["dots"])
        for dot in dots:
            all_dots.append(["G",dot[0],dot[1]])

    elif row["dots"] < 0:

        dots = gen_dot(row["ctuid"], -row["dots"])
        for dot in dots:
            all_dots.append(["L",dot[0],dot[1]])

    else:

        None

pd.DataFrame(all_dots, columns = ['T','X','Y']).to_csv("dots100.csv")
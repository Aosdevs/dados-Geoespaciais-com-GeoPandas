import geopandas as gpd
import matplotlib.pyplot as plt

data = gpd.read_file('Dados/SP_Municipios_2020.shp')

data.head(5)

data.plot
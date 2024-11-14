class LuccMEModel:

    def __init__(self, gdf, index_name):
        
        self.gdf = gdf
        self.gdf.set_index(index_name, inplace=True)

        self.wr = weights.contiguity.Queen.from_dataframe(self.gdf, use_index=True)

    def neighs (self, row):
        return self.gdf.loc[self.wr.neighbors[row.name]]

from geopandas import GeoDataFrame
from pysal.lib import weights

class GeoLuccDataFrame (GeoDataFrame):

    def __init__(self, data=None, *args, id_name, geometry=None, crs=None , **kwargs):
        if (
            kwargs.get("copy") is None
            and isinstance(data, GeoDataFrame)
            and not isinstance(data, GeoLuccDataFrame)
        ):
            kwargs.update(copy=True)
        
        super().__init__(data, *args, **kwargs)
        self.set_index(id_name, inplace=True)
        self._wr = None

    def create_neighborhood(self):
        self._wr = weights.contiguity.Queen.from_dataframe(self, use_index=True)

    def neighs (self, idx):
        return self.loc[self._wr.neighbors[idx]]


import geopandas as gpd
import pandas as pd


gdf = gpd.read_file("../data/cs_moju/cs_moju.shp")
cs_moju = GeoLuccDataFrame(gdf, id_name="object_id_")

cs_moju.create_neighborhood()


lutypes = ["f", "d", "o"]
df = pd.DataFrame()
for lu in lutypes:
    serie = cs_moju.apply (lambda row: cs_moju.neighs(row.name)[lu].mean(), axis=1)
    df[lu] = serie


df.sort_values(by='f', inplace=True, ascending=False)
print (df.head())


#cs_moju.apply (lambda row: (cs_moju.neighs(row.name)["f"]).mean(), axis=1)
#cell = cs_moju.loc["C100L178"]
#print (cell)
#neighs = cs_moju.neighs(cell.name)
#print (neighs["f"].mean())
#print (cs_moju._wr.neighbors)
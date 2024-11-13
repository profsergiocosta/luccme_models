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
        self._wr = weights.contiguity.Queen.from_dataframe(gdf, use_index=True)


import geopandas as gpd


gdf = gpd.read_file("../data/cs_moju/cs_moju.shp")
cs_moju = GeoLuccDataFrame(gdf, id_name="object_id_")

cs_moju.create_neighborhood()

print (cs_moju.head())
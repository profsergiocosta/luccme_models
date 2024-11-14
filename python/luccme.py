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
        self.neighs_ = None

    # custo alto de memoria
    def create_neighborhood(self):
        neighbors = weights.contiguity.Queen.from_dataframe(self, use_index=True).neighbors
        values = map(lambda idx: self.loc[idx], neighbors.values())
        self.neighs_ = dict(zip(neighbors.keys(), values))

    def neighs (self, idx):
        return self.neighs_[idx]



import geopandas as gpd
import pandas as pd

import salabim as sim

'''

cs_moju.create_neighborhood()


lutypes = ["f", "d", "o"]
df = pd.DataFrame()
for lu in lutypes:
    serie = cs_moju.apply (lambda row: cs_moju.neighs(row.name)[lu].mean(), axis=1)
    df[lu] = serie

#df.sort_values(by='f', inplace=True, ascending=False)
#print (df.head())


#cs_moju.apply (lambda row: (cs_moju.neighs(row.name)["f"]).mean(), axis=1)
#cell = cs_moju.loc["C100L178"]
#print (cell)
#neighs = cs_moju.neighs(cell.name)
#print (neighs["f"].mean())
#print (cs_moju._wr.neighbors)

class PotentialDNeighSimpleRule (sim.Component):
    def setup(self, valor):
        print ("criando")
        self.valor = valor

    def process(self):
        while True:
            print(f"[Tempo {env.now()} {self.valor}] ")
            self.hold(1)

    '''




class PotentialDNeighSimpleRule (sim.Component):

    def setup(self):
        print ("criando a vizinhança")
        env.cs.create_neighborhood()


    def process(self):
        while True:
            print(f"[Tempo {env.now()} ] ")
            for lu in env.landUseTypes:
                serie = env.cs.apply (lambda row: env.cs.neighs(row.name)[lu].mean(), axis=1)
                env.pcs[lu] = serie
            self.hold(1)


# criar uma subclasse para explicitar os parametros
env = sim.Environment()

env.cs = GeoLuccDataFrame(
    gpd.read_file("../data/cs_moju/cs_moju.shp")[["object_id_","geometry","f", "d", "o"]], 
    id_name="object_id_"
)

env.pcs = pd.DataFrame()

env.landUseTypes = ["f", "d", "o"]

pt = PotentialDNeighSimpleRule()

'''
def neighs (idx):
    return env.cs.loc[idx]

valores_mapeados = list( map(neighs, env.cs._wr.neighbors.values()) )
dic = dict(zip(env.cs._wr.neighbors.keys(), valores_mapeados))
'''



env.run(till=5)
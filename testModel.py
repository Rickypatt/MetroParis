from model.fermata import Fermata
from model.model import Model

model = Model()
model.buildGraph()
print("Num nodi:", model.getNumNodi())
print("Num archi:", model.getNumArchi())

f = Fermata(2,"Abbesses",2.33855, 48.8843)
nodesBFS = model.getBFSTree(f)
for n in nodesBFS:
    print(n)


archiMaggiori = model.getArchiPesoMaggiore()
for a in archiMaggiori:
    print(a)
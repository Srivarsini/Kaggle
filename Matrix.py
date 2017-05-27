import csv
from scipy.cluster.hierarchy import cophenet
from scipy.spatial.distance import pdist

with open('../mergedData.csv', 'rb') as f:
    reader = csv.reader(f)
    data_as_list = list(reader)

Z = linkage(data_as_list, 'ward')

c, coph_dists = cophenet(Z, pdist(data_as_list))

c



# -*- coding: utf-8 -*-
"""
Created on Sat May 27 00:39:06 2017

@author: Sriva
"""

import csv
from sklearn import preprocessing
from scipy.cluster.hierarchy import cophenet
from scipy.spatial.distance import pdist
from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
import pandas as pd

with open('mergedData.csv', 'rb') as f:
    reader = csv.reader(f)
    data_as_list = list(reader)

le=preprocessing.LabelEncoder()
df = pd.DataFrame(data_as_list)
print type(df)

for col in df.columns.values:
       # Encoding only categorical variables
       if df[col].dtypes=='object':
       # Using whole data to form an exhaustive list of levels
           data=df[col]
           le.fit(data.values)
           df[col]=le.transform(df[col])
       #X_test[col]=le.transform(X_test[col])
print len(df)
#Z = linkage(data_as_list, 'ward')

#c, coph_dists = cophenet(Z, pdist(data_as_list))

#c

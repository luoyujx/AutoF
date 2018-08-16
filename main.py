import pandas as pd
from io import StringIO
from sklearn import linear_model

import matplotlib.pyplot as plt
import regression2D as regr
import dataprocessor as DP

# set ion database

# set root file

data = DP.refresh()
print (data)
(a,b,r)=regr.Linear.getline(data, 'MtZ', 'ToF')
output = 'a='+str(a)+' b='+str(b)+' r='+str(r)
print(output)
regr.Linear.getgraph(data, 'MtZ', 'ToF')
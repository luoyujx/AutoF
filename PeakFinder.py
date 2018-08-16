import math
import plotly.plotly as py
import plotly.graph_objs as go
from plotly.tools import FigureFactory as FF

import numpy as np
import pandas as pd
import scipy
import peakutils
from numpy import histogramdd

from pyspark.sql import SparkSession, DataFrame
from pyspark.sql.functions import udf, explode
import matplotlib.pyplot as plt
from numpy import histogramdd

print('finding peaks on file origin.csv')
pdf = pd.read_csv('origin.csv')
time_series = pdf['t']
time_series = time_series.tolist()


hist, (xedges, yedges) = histogramdd(
    (pdf['t'], pdf['x']),
    bins=(1000, 1000),
    range=((0, 8000), (-50, 50))
)


x=(xedges[1:]+xedges[:-1])/2
y=hist.sum(1)
    
indixes = peakutils.indexes(y, thres=100, min_dist=5,thres_abs=True)
print(indixes)


#plt.scatter(data[x], data[y], color='blue')
plt.plot((xedges[1:]+xedges[:-1])/2, hist.sum(1), indixes)
plt.scatter(x[indixes], y[indixes], color='red')
plt.xlim(0, 4000)
plt.grid(True)
plt.yscale("log")

plt.tight_layout()
plt.show()








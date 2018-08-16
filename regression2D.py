import pandas as pd
import matplotlib.pyplot as plt

from io import StringIO
from sklearn import linear_model

# 2D regression

# linear regression
class Linear:
    
    def getline(data, x, y):
        """
        get a, b, and r of the regression
        """    

        # read data
        X = data.loc[:, [x]].values
        Y = data[y].values

        # perform linear regression
        regr = linear_model.LinearRegression()
        regr.fit(X,Y)
 
        # get the slope and the intercept of the line
        a, b, r = regr.coef_, regr.intercept_, regr.score(X, Y)
        return a, b, r
    
    # regression with graph plotted
    def getgraph(data, x, y):
        """
        plot the linear regression line
        """

        # read data
        X = data.loc[:, [x]].values
        Y = data[y].values

        # perform linear regression
        regr = linear_model.LinearRegression()
        regr.fit(X,Y)

        # drawing
        # 1.real spots
        plt.scatter(data[x], data[y], color='blue') 
        # 2.regression line
        plt.plot(data[x], regr.predict(X), color='red', linewidth=4)
        plt.show()
     


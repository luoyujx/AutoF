import pandas as pd
from sklearn import linear_model
import particles

import matplotlib.pyplot as plt
import regression2D as regr


def loaddata(file):
    data = pd.read_csv(file, sep=",")
    return data

peakdata=loaddata('peaks1.csv')
peaks=peakdata.loc[:, ['Peaks']].values
totalpeaks=peaks.shape[0] #gives number of row count

iondata=particles.output()
mtz=iondata.loc[:, ['RootMtoZ']].values
totalions=mtz.shape[0]

data = pd.DataFrame([[0, 623.87,0],[11.26518841,5283.7,0]],columns = ['MtZ', 'ToF', 'Error'])
(a, b, r)=regr.Linear.getline(data, 'MtZ', 'ToF')

def loaddata(file):
    data = pd.read_csv(file, sep=",")
    return data

def ionmaching(peaknumber):
    output = pd.DataFrame() 
    for i in (range(0,totalions)):
        x = mtz[i,0]
        y = peaks[peaknumber,0]
        d=abs((x-(y-b)/a)[0])
        if d<((y-b)/a*0.025):
            output=output.append([[i,d]])
        else:
            continue    
    return output            
           

def refresh():
    n=0
    data1 = data    
    for k in (range(1,totalpeaks)):
        df = ionmaching(k)
        if df.shape[0] == 0:
            continue
        else:
            d=0
            for i in range(df.shape[0]):
                b=df.iat[i,0]
                lable=iondata.index[b]
                print (lable)
                indexlable=str(lable)
                c=iondata.columns.get_loc('RootMtoZ')
                d=peakdata.columns.get_loc('Peaks')
                adddata=pd.DataFrame([[iondata.iat[b,c], peakdata.iat[k,d], df.iat[i,1]]],
		    		index = [indexlable], columns = ['MtZ', 'ToF', 'Error'])   
                data1=data1.append(adddata)
            n=n+1
            print('find'+str(n)+'th peak, peak No.'+str(k)+', ToF='+str(peakdata.iat[k,d]))    
            #print(data1)
    return data1

#def refreshslope():

#def createion():


import pandas as pd
import math
import itertools

c=12.0107
h=1.00794
o=15.999
i=126.90447
he=4.002602

class ion:
    
    def mass(C,H,O,I,He):
        mass=c*C+h*H+O*o+i*I+he*He
        return mass
    
    def MtZ(C,H,O,I,He,P):
        mass=ion.mass(C,H,O,I,He)
        MtZ=(mass/P)**(1/2)
        return MtZ
    
    def name(C,H,O,I,He,P):
        output=''
        series=[C,H,O,I,He,P]
        atomnames=['C','H','O','I','He','P']
        for i in range(5):
            if series[i]>1:
                a=atomnames[i]
                b=str(series[i])
                output=output+a+b
            elif series[i]==1:
                a=atomnames[i]
                output=output+a
        if P>0:
            output=output+'_'+str(P)+str(atomnames[5])            
        return output

def water():
    data=pd.DataFrame()
    for (i,j,k) in itertools.product(range(0,4), repeat=3):
        if i==0 and j==0:
            continue
        if i>2:
            continue
        elif j>1:
            continue
        elif k==0 or k>2:
            continue    
        else:    
            name=ion.name(0,i,j,0,0,k)
            MtZ=ion.MtZ(0,i,j,0,0,k)
            adddata=pd.DataFrame([[MtZ]],index=[name],columns = ['RootMtoZ'])
            data=data.append(adddata)                
    return data

def helium():
    data=pd.DataFrame()
    for i in range(1,4):
        name=ion.name(0,0,0,0,1,i)
        MtZ=ion.MtZ(0,0,0,0,1,i)
        adddata=pd.DataFrame([[MtZ]],index=[name],columns = ['RootMtoZ'])
        data=data.append(adddata)                
    return data

def molecule():
    data=pd.DataFrame()
    for (i,j,k,l) in itertools.product(range(0,10), repeat=4):
        if l>3:
            if (i,j,k,)==(0,0,1):
                name=ion.name(i,j,0,k,0,l)
                MtZ=ion.MtZ(i,j,0,k,0,l)
                adddata=pd.DataFrame([[MtZ]],index=[name],columns = ['RootMtoZ'])
                data=data.append(adddata)
            else:
                continue    
        elif (i,j,k)==(0,0,0):
            continue
        elif i>1 or j>2 or k>2 or l==0:
            continue
        elif (i,j,k)==(0,1,0) and l>1:
            continue       
        else:    
            name=ion.name(i,j,0,k,0,l)
            MtZ=ion.MtZ(i,j,0,k,0,l)
            adddata=pd.DataFrame([[MtZ]],index=[name],columns = ['RootMtoZ'])
            data=data.append(adddata)                
    return data

def output():
    data = helium()
    data1 = molecule()
    data2 = water()
    data=data.append(data1)
    data=data.append(data2)
    return data

   





# coding: utf-8

# In[8]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df=pd.read_csv("S:/extra/SIH/tsunami/Earthquake.csv",sep=',',header=0)

df=df.drop(['time','locationSource','magSource','magType','nst','gap','dmin','rms','net','id','updated','type','horizontalError','magNst','status','depthError','magError'], axis=1)

#print(df.columns)

#print(df.head())

#df2=df['mag']>6

#print(df2)

df['mag'].describe()

df2=df.loc[df['mag'] > 6]

print(df2)


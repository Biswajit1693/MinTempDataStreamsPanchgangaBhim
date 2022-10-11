import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
tb1=pd.read_csv(r'C:\Users\dell\Documents\PYTHON\Data for python\water_quality_of_tributary_streams_panchganga_and_bhima-2014.csv',
                usecols=["TEMPERATURE ºC  : Min"])
minarr=np.array(tb1)
print(minarr)
y,edge=np.histogram(minarr)
print(edge)
print(y)
mid=0.5*(edge[1:]+edge[:-1])
print(mid)
tb1.plot(kind='hist',y='TEMPERATURE ºC  : Min',edgecolor='black',linestyle='--',linewidth=1,)
plt.plot(mid,y)
plt.xlabel("Min Temperature ")
plt.title("Temperature Records for Panchganga & Bhima during 2014")
plt.show()
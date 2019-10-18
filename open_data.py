# This code is to calculate the speed from the pulse signal
# Copyright 2019 Roman Babenko <kubox61@gmail.com>
import pandas as pd
import matplotlib.pyplot as plt
from PyEMD import EMD
import numpy as np
s = np.random.random(100)
emd = EMD()
IMFs = emd(s)
IMFs.plot()
NUMBER_LABELS = 8
data = pd.read_csv("speed_impuls.txt", sep="\t", header=None, decimal=',')
len_data = data.shape[0]
print (len_data)
data_zero = pd.DataFrame(0, index=range(data.shape[0]), columns=range(1)) # create zero DataFrame
data_impuls = pd.concat([data[0],data_zero],axis=1,ignore_index=True)
time_impuls = pd.Series()

for x in range(2,len_data,1):
    if data.iloc[x,1]>1 and data.iloc[x-1,1]<1:
        data_impuls.iloc[x,1] = 1
        time_impuls = time_impuls.append(pd.Series([data.iloc[x,0]]))
print(time_impuls)
len_data = time_impuls.size
print(time_impuls.iloc[4])
data_speed = pd.DataFrame(0, index=range(len_data), columns=range(2))

for x in range(len_data,NUMBER_LABELS+1,-1):
    data_speed.iloc[x-1-NUMBER_LABELS-1, 0] = time_impuls.iloc[x-1]
    data_speed.iloc[x-1-NUMBER_LABELS, 1] = 1/(time_impuls.iloc[x-1] - time_impuls.iloc[x-1-NUMBER_LABELS])
#data_speed.to_hdf('savefile.h5', 'table', mode='w')
print (data)
print (data_zero)
print (data_impuls)
print (time_impuls)
print (data_speed)
data[1].plot()
data_impuls[1].plot()
data_speed.plot()
plt.show()

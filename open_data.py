import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("speed_impuls.txt", sep="\t", header=None, decimal=',')
l1 = data.shape[0]    # count row
print (l1)
#data_zero = pd.DataFrame(0, index=range(data.shape[0]), columns=range(data.shape[1])) # create zero DataFrame
data_zero = pd.DataFrame(0, index=range(data.shape[0]), columns=range(1)) # create zero DataFrame
data_2 = pd.concat([data[0],data_zero],axis=1)
for x1 in range(2,l1,1):
    if data.iloc[x1,0]>1 and data.iloc[x1-1,1]<1:
        data_2.iloc[x1,1] = 1
#data_zero[0:] = data[0:]
#data.loc[1,1] = data
#data_zero['0'] = data['0'].values
print(data)
print(data_zero)
print (data_2)
data[1].plot()
data_2
plt.show()
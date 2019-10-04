import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("speed_impuls.txt", sep="\t", header=None, decimal=',')
l1 = data.shape[0]    # count row
print (l1)
#data_zero = pd.DataFrame(0, index=range(data.shape[0]), columns=range(data.shape[1])) # create zero DataFrame
data_zero = pd.DataFrame(0, index=range(data.shape[0]), columns=range(1)) # create zero DataFrame
data_2 = pd.concat([data[0],data_zero],axis=1,ignore_index=True)
#t = pd.Series(0, index=range(0))
t = pd.Series()
for x1 in range(2,l1,1):
    if data.iloc[x1,1]>1 and data.iloc[x1-1,1]<1:
        data_2.iloc[x1,1] = 1
        t = t.append(pd.Series([data.iloc[x1,0]]))
#        t = [t, data.iloc[x1,0]]
print(t)
l2 = t.size
print(t.iloc[4])
data_speed = pd.DataFrame(0, index=range(l2), columns=range(2))
for x2 in range(l2,7,-1):
#    data_speed.iloc[x2-6,0] = t[x2]
#    data_speed.iloc[x2-6,1] = 1/(t[x2]-t[x2-6])
    data_speed.iloc[x2 - 6, 0] = t.iloc[x2-1]
    data_speed.iloc[x2-6,1] = 1/(t.iloc[x2-1]- t.iloc[x2-7])
#data_zero[0:] = data[0:]
#data.loc[1,1] = data
#data_zero['0'] = data['0'].values
print (data)
print (data_zero)
print (data_2)
print (t)
print (data_speed)
data[1].plot()
data_2[1].plot()
data_speed.plot()
plt.show()
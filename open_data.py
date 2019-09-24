import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("speed_impuls.txt", sep="\t", header=None, decimal=',')
print(data)
data.plot()
plt.show()
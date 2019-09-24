import pandas as pd

data = pd.read_csv("speed_impuls.txt", sep="\t", header=None)
print(data)
plot(data)
import matplotlib.pyplot as plt
import math
import copy
import os
import numpy as np 
import pandas as pd
import matplotlib
#based on: Chapter 6 Monte Carlo simulations
#THIS PLOTS A GRAPH TO TEST IF THE RANDOMLY GENERATED VALUES ARE TRULY RANDOM
list_of_powers=np.random.random_integers(0,99, size=(100))
#can vary (0,99) for the range of min and max values respectively. Vary size=(100) to vary number of points to plot
print(list_of_powers)
x=[]
y=[]
for i in range(len(list_of_powers)):
    x.append(list_of_powers[i])
for i in range(len(list_of_powers)-1):    
    y.append(list_of_powers[i+1])
y.append(list_of_powers[0])
#########################
#TO STORE DATA USING PANDA
data=[]
if len(x)<=len(y):
    for i in range(len(x)):
        sub=[]
        sub.append(x[i])
        sub.append(y[i])
        data.append(sub)
df = pd.DataFrame(data, columns=['x', 'y'])
df.to_pickle("Output_Data.csv")
#USING DATA IN PANDA TO PLOT
plot_x=[]
plot_y=[]
for row in df["x"]:
    plot_x.append(row)
for row in df["y"]:
    plot_y.append(row)
#TO PLOT
plt.scatter(plot_x,plot_y)
plt.xlabel("x_{i}")
plt.ylabel("x_{i+1}")
plt.show()
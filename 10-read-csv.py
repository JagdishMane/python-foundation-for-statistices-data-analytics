import os 
import pandas as pd
# carbon = pd.read_csv('http://stat4ds.rwth-aachen.de/data/Carbon.dat', sep='\s+')
carbon = pd.read_csv('./10-carbon.csv', sep='\s+')
print(carbon)
print(carbon.shape)
print(carbon.columns)
print(carbon.head())
print(carbon.tail())
print(carbon.describe())
c_mean = carbon['CO2'].mean()  ## Average of a set of numbers
print(c_mean)
print(carbon['CO2'].std())     ## Amount of variabtion in set of values  -- How much the value deviate from the mean.(average)
## 1) Find mean
## 2) Subtract the mean from each data point and square the result
## 3) Calculate the average of the squared differences
## 4) Take the square root of this average.

## \singma = \sqrt{\frac{\sum (x_i - \mu)^2}{n}}

print(carbon['CO2'].median())   ## To find Middle value of a dataset.

import matplotlib.pyplot as plt
plt.hist(carbon['CO2'], density=True, bins=8)
plt.ylabel('Proportion')
plt.xlabel('CO2');
plt.title('Histogram of CarbonDF[CO2]')
#plt.show()

fig1, ax1 = plt.subplots()
plt.xlabel('CO2 values')
ax1.boxplot(carbon['CO2'],vert=False)
plt.show()
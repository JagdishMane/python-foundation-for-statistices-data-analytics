import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
GS = pd.read_csv('http://stat4ds.rwth-aachen.de/data/Guns_Suicide.dat',sep='\s+')
GS.info()
GS.plot(kind='scatter', x='guns', y='suicide', color='blue', figsize=(10, 7))
plt.xlabel('guns', size=14)
plt.ylabel('suicide', size=14) 
print(GS.corr()) # correlation matrix for pairs of variables in GS data file
#plt.show()
##   ================== ##

import statsmodels.formula.api as sm  # fit linear regression
mod = sm.ols(formula='suicide ~ guns', data=GS).fit() # model parameter estimates
print(mod.params)
print(mod.summary())
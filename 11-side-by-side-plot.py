import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#crime = pd.read_csv('http://stat4ds.rwth-aachen.de/data/Murder2.dat', sep='\s+')
crime = pd.read_csv('./11-crime.csv', sep='\s+')

sns.boxplot(x='murder', y='nation', data=crime, orient='h')
crime.groupby('nation')['murder'].describe()


plt.xlabel('Murder Rate')
plt.ylabel('Nation')
plt.title('Boxplot of Murder rate by nation')
plt.show()
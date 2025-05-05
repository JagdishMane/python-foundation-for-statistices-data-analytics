import numpy as np
import pandas as pd
import matplotlib as plt
PID = pd.read_csv('http://stat4ds.rwth-aachen.de/data/PartyID.dat', sep='\s+')
PID_table = pd.crosstab(PID['race'], PID['id'])
print(PID_table)

# Marginals in Statistical Analysis: Knowing the marginal totals is 
# crucial when evaluating the probability distributions across categories
#  and preparing for statistical tests like the Chi-square test of independence.
## cipy.stats.contingency: A module within SciPy, a scientific computing library, that provides functions to work with contingency tables.
from scipy.stats.contingency import margins ## Find marginal
mr, mc = margins(PID_table)   # dist. counts
print(mr)  ## row marginal counts == Sum of total rows
print(mc)  ## column marginal counts == sum of total columns



## Derivation of joint probability table:
### np.array(PID_table Converts the Table into Numpy Array
print(np.array(PID_table))
print(sum(sum(np.array(PID_table))))
asarray=np.array(PID_table)/sum(sum(np.array(PID_table)))
prob_table=pd.DataFrame(asarray, columns=["Democrat","Independent","Republican"])
prob_table.index=["black", "white", "other"]
print(prob_table)


## Derivation of conditional row probabilities (within row) tables:
asarray1=np.array(PID_table)/mr
pb1=pd.DataFrame(asarray1, columns=['Democrat',"Independent","Republican"])
pb1.index=["black","white","other"]
print(pb1)

## Derivation of conditional row probabilities (within column) tables:
asarray1=np.array(PID_table)/mc
pb1=pd.DataFrame(asarray1, columns=['Democrat',"Independent","Republican"])
pb1.index=["black","white","other"]
print(pb1)

### Contigency table in statsmodels:
import statsmodels.api as sm
PIDtable = sm.stats.Table.from_data(PID)
print(PIDtable)

from statsmodels.graphics.mosaicplot import mosaic
fig, _ = mosaic(PID, index=['race', "id"])
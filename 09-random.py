import random
rlist = random.sample(range(1,60), 5)
print(rlist)

import numpy as np
y = list(range(1,60))
rlist2 = np.random.choice(y, 5)
print(rlist2)
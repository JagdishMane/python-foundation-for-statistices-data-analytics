import numpy as np
import matplotlib.pyplot as plt
mu, sigma = 100, 16
y1=np.random.normal(mu, sigma, 30)
print(f"{y1.mean()}, {y1.std()}")

plt.hist(y1, bins='auto')
print(plt.hist(y1, bins='auto'))
plt.show()
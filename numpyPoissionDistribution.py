import seaborn as sb
import matplotlib.pyplot as plt
from numpy import random as rd

#parameter: lam(number of occurance or rate) , size
arr = rd.poisson(lam=2, size=10)
print(arr)

#Visualization of poission dist
sb.distplot(rd.poisson(lam=2, size=1000), kde=False)
plt.show()

#poission vs normal visualization
sb.distplot(rd.poisson(lam=50, size=1000), hist=False)
sb.distplot(rd.normal(loc=50,scale=7, size=1000), hist=False)
plt.show()
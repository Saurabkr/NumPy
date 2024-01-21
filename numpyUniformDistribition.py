import seaborn as sb
import matplotlib.pyplot as plt
from numpy import random as rd

#parameter: 
arr = rd.uniform(size=10)
print(arr)

#Visualization of poission dist
sb.distplot(rd.uniform(size=1000), hist=False)
plt.show()
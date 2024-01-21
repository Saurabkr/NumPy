import seaborn as sb
import matplotlib.pyplot as plt
from numpy import random as rd

#parameter: 
arr = rd.logistic(loc=1, scale=2, size=(2,3))
print(arr)

#Visualization of logistic dist
sb.distplot(rd.logistic(size=1000), hist=False)
plt.show()
import seaborn as sb
import matplotlib.pyplot as plt
from numpy import random as rd

arr = rd.normal(size=(2,3))
arr1 = rd.normal(loc=1,scale=2,size=(2,3))
print(f'2D array :\n',arr)
print(f'2D array with mean(loc) & standard median(scale):\n',arr1)

#Normal(Gaussian) distribution or Bell graph
sb.distplot(rd.normal(size=(2,3)),hist=False)
plt.show()

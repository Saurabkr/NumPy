import matplotlib.pyplot as plt
import seaborn as sb
from numpy import random as rd

arr = rd.binomial(n=10, p=0.5, size=12)
print("Binomial distribution with number of trial(n), probability(p) and size:\n",arr)

#Binomial dist = discrete dist visualization
sb.distplot(rd.binomial(n=10, p=0.8, size=1000), hist=True, kde=False)
plt.show()

#compare binomial dist(size= 500) and nrml dist(size=100)

sb.distplot(rd.binomial(n=12, p=0.6, size=500),hist=False, label='Binomial')
sb.distplot(rd.normal(loc=1, scale=5, size=100),hist=False, label='Normal')
plt.show()
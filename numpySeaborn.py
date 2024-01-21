import seaborn as sb
import matplotlib.pyplot as plt

sb.distplot([1,2,3,4,5])
plt.show()

#print graph without histogram
sb.distplot([1,2,3,4,5], hist=False)
plt.show()


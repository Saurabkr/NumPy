import numpy as np

#Truncate: Towards zero in number line
arr = np.trunc([2.346, -4.879])
print(arr)

#Fix() - same as truncate
arr1 = np.fix([2.346, -4.879])
print(arr1)

#Rounding off : around(value,upto which digit)
arr3 = np.around(3.457,2)
print(arr3)

#floor() : towards left
arr4 = np.floor([2.346, -4.879])
print(arr4)

#ciel : towards right
arr5 = np.ceil([2.346, -4.879])
print(arr5)
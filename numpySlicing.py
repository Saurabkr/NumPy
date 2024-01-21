import numpy as np

arr = np.array([2,5,7,8,9,3])

print(arr[::2])
print(arr[-3:-1])

arr1 = np.array([[1,3,5,7],[2,4,6,8]])
#To slice subarray from particular row
print(arr1[0,1:-1], arr1[1,2:]) 

#To slice the 2nd to 4th element form all row of 2-D array
arr2 = np.array([[2,3,4,6,4],[4,7,9,6,4],[1,2,3,4,5]])

print(arr2[0:3, 1:4])
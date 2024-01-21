import numpy as np

#reshaping from 1-D to 2-D
arr = np.array([2,3,4,5,6,7,7,9])
arrReshape = arr.reshape(2,4)
print('After reshaping:',arrReshape)

#reshaping from 1-D to 3-D
arr2 = np.array([2,5,44,7,93,6,73,5,3,83,6,34])
arrReshape2 = arr2.reshape(2,2,3)
print('After reshaping:',arrReshape2)

#Reshaping from any n-D to 1-D

arr1 = np.array([[[2,5,44],[7,93,6]],[[73,5,3],[83,6,34]]])
arrReshape1 = arr1.reshape(-1)
print('After reshaping:',arrReshape1)
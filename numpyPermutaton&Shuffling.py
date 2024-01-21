import numpy as np
from numpy import random as rd

#In shuffle() we perform a change in original array
arr = np.array([2,3,5,6,8])
rd.shuffle(arr)
print(f'Shuffled original array:\n', arr)

#But in permutation we do not change original array
arr1 = np.array([0,9,8,6])
print(f'Shuffled array:\n',rd.permutation(arr1))
print("Original array not changed :\n",arr1)
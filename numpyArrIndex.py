import numpy as np

arr = np.array([1,2,3,5,6])

#To access 3rd element
print("3rd element:",arr[2])

arr1 = np.array([[2,3,5,8],[8,5,6,2]])

#To access 3rd column element from 2nd row
print("3rd column element from 2nd row:",arr1[1,2])

arr2 = np.array([[[2,5,44],[7,93,6]],[[73,5,3],[83,6,34]]])

#To access 34 from 3-D array
print("34 from 3-D array:",arr2[1,1,2])
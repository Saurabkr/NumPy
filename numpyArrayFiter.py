import numpy as np

#Process to filter by attaching boolean indexing
arr = np.array([1,5,7,8,4,5])
arrIndex = [True, False, True,True,False,False]
arrNew = arr[arrIndex]
print(f'Array which have true indexing will get printed:\n{arrNew}') 

#We will understand filtering based on conditions
arr1 = np.array([23,4,5,66,74,3,4,66,98,11])
arrEmpty = []

for i in arr1:
    if i > 20:
        arrEmpty.append(True)
    else:
        arrEmpty.append(False)

arrFiltered = arr1[arrEmpty]
print(f'Element that have true indexes we get printed: \n{arrFiltered}')

#We can do filtering directly too

arr1 = np.array([23,4,5,66,74,3,4,66,98,11])
arrEmpty1 = arr1 > 20
arrFilter1 = arr1[arrEmpty1]
print(f'Direct method to filter true indexes element: \n{arrFilter1}')


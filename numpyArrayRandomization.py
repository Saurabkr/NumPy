from numpy import random as rd
#Generate random integer
arrRand = rd.randint(100)
print(f'Random integer type number : \n{arrRand}')

arrRandFloat = rd.rand()
print(f'Random float type number : \n{arrRandFloat}')

#we can print random element in 1-D array 
arrRandList = rd.randint(100, size=(10))
print(f'Random integer type 1D array : \n{arrRandList}')
arrRandListf = rd.rand(5)
print(f'Random float type 1D array : \n{arrRandListf}')

#we can print random element in 2-D array 
arrRandList1 = rd.randint(100, size=(3,4))
print(f'Random integer type 2D array : \n{arrRandList1}')
arrRandList1f = rd.rand(3,4)
print(f'Random float type 2D array : \n{arrRandList1f}')

#We can also select random number from given set of element
arrChoice = rd.choice([2,4,5,6,7,8,1])
print(f'Element is form given set of element: \n{arrChoice}')

arrChoice2 = rd.choice([2,4,5,6,7,8,1],size=(3))
print(f'1D array from given set of element: \n{arrChoice2}')

#For 2D array from given element set
arrChoice1 = rd.choice([2,4,5,6,7,8,1],size=(2,3))
print(f'2D array is from given set of element: \n{arrChoice1}')

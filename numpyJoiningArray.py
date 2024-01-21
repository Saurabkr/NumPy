import numpy as np

arr = np.array([2,3,4,5])
arr1 = np.array([7,9,8,6])

joinedArray = np.concatenate((arr,arr1))
print(joinedArray)

#concatenate row wise
arr2 = np.array([[2,3],[4,5]])
arr3 = np.array([[7,9],[8,6]])
joinedArray1 = np.concatenate((arr2,arr3), axis=1)
print(joinedArray1)

#concatenate column wise
arr4 = np.array([[2,3],[4,5]])
arr5 = np.array([[7,9],[8,6]])
joinedArray2 = np.concatenate((arr4,arr5), axis=0)
print(joinedArray2)

#stack , vstack, hwstack
arrS = np.array([[2,3],[7,8]])
arrS1 = np.array([[4,1],[9,3]])

arrJoin = np.stack((arrS,arrS1))
arrJoin1 = np.hstack((arrS,arrS1))
arrJoin2 = np.vstack((arrS,arrS1))

print(arrJoin)
print(arrJoin1)
print(arrJoin2)

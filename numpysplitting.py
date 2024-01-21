import numpy as np

arr = np.array([2,3,4,5,6,7])
arrSplit = np.array_split(arr, 4) #array_split is intelligent too 
print(arrSplit)
#Access the splitted array
print(arrSplit[0])
print(arrSplit[1])
print(arrSplit[2])
print(arrSplit[3])

#Split 2-D array

arr1 = np.array([[4,3,2],[3,5,6],[3,5,9],[3,2,1]])
arrSplit1 = np.array_split(arr1,3)
arrSplit3 = np.array_split(arr1,3, axis=1)
print("Splitted 2D array: \n", arrSplit1)
print(arrSplit1[0])
print(arrSplit1[1])
print(arrSplit1[2])

print("Splitted 2D array using axis: \n", arrSplit3)
print(arrSplit3[0])
print(arrSplit3[1])
print(arrSplit3[2])

#Use vsplit and hsplit
arr2 = np.array([[4,3,2],[3,5,6],[3,5,9],[3,2,1]])
arrSplit2 = np.hsplit(arr2,3)
print("Splitted 2D array using hsplit: \n", arrSplit2)
print(arrSplit2[0])
print(arrSplit2[1])
print(arrSplit2[2])




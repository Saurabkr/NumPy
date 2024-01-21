import numpy as np

arr = np.array([2,3,4,5,6,7,7,9])

#Iterating over 1-D array
for i in arr:
    print(i)

arr1 = np.array([[[2,5,44],[7,93,6]],[[73,5,3],[83,6,34]]]) 

#Scaler iterating in 3-D array
for i in arr1:
    for j in i:
        for k in j:
            print(k)

# Iteration using nditer()
arr2 = np.array([[[21,53,44],[72,93,66]],[[73,57,39],[83,61,34]]])     

for i in np.nditer(arr2):
    print(i)

#Also we can perform slicing here
for i in np.nditer(arr2[:,:,::2]): 
    print(i)



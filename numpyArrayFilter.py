import numpy as np

#1-D array sorting
arr = np.array([23,45,67,90,12])

arrSorted = np.sort(arr)
print(f'Sorted array: {arrSorted}')

#2-D array sorting

arrD = np.array([[23,45,13],[98,14,65],[75,98,24]])

arrdSorted = np.sort(arrD)
print(f"2D sorted array: {arrdSorted}")
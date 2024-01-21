from numpy import random as rd

#Random distribution 
#Set the probability of each type
#2->0.3, 3->0.5, 6->0.1, 8->0.1
arr = rd.choice([2,3,6,8], p=[0.3,0.5,0.15,0.05], size=(100))
print(f'1-D Array based on probability : \n{arr}')

arr1 = rd.choice([2,3,6,8], p=[0.2,0.7,0.1,0.0], size=(4,3))
print(f'2-D Array based on probability : \n{arr1}')



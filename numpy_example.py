import numpy as np
a = np.array([1, 2, 3])             # array 1
print(a)
print(type(a))
x = [1, 2, 3, 4]                # list to array
y = np.array(x)
print(y)
print(type(y))
l = []
for i in range(1, 5):                   # user input array
    val = input("enter value: ")
    l.append(val)
arr = np.array(l)
print(arr)
print(type(arr))
y = np.array([1,2,3,4,5,6,7,8,9,10])                               # 1Dimension array
print(y)
print(type(y))
print(y.ndim)
x = np.array(
    [
        [1,2,3,4,5,6,7,8,9,10],
        [1,2,3,4,5,6,7,8,9,10]
        ])     # 2`Dimension array
print(x)
print(type(x))
print(x.ndim)
a = np.array( [
        [
            [
   [1,2,3,4,5,6,7,8,9,10],
        [1,2,3,4,5,6,7,8,9,10]                          # 3`Dimension array
                
            ]

        ]
        ])
print(a)

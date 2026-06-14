import numpy as np

# 1D Array
a = [1, 2, 3, 4, 5, 6, 7]
y = np.array(a)

print(y)
print(type(y))
print(y.ndim)

# 2D Array
x = np.array([
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5]
])

print(x)
print(x.ndim)

# 3D Array
y1 = np.array([
    [
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5]
    ]
])

print(y1)
print(y1.ndim)

# 14-Dimensional Array
n = np.array([1, 2, 3, 4, 5], ndmin=14)

print(n)
print(n.ndim)
#How to Create NumPy Array using NumPy Function
a_zeros = np.zeros(10)
print(a_zeros)
print()
a_zeros1 = np.zeros((3,4))
print(a_zeros1)
a_one = np.ones(7)
print(a_one )
print()
a_one1 = np.ones((4,3))
print(a_one1 )
em = np.empty(4)
print()
print(em)
rn = np.arange(4)
print(rn)
di = np .eye(3)
print(di)
print()
di1 = np .eye((3,1))
print(di1)
l = np.linspace(7)
print(l)
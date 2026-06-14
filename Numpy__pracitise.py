import numpy as np
a = [1, 2, 3, 4, 5, 6, 7]# 1D Array
y = np.array(a)
print(y)
print(type(y))
print(y.ndim)
x = np.array([                      # 2D Array
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5]
])
print(x)
print(x.ndim)
y1 = np.array([             # 3D Array
    [
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5]
    ]
])
print(y1)
print(y1.ndim)
n = np.array([1, 2, 3, 4, 5], ndmin=14)   # 14-Dimensional Array                                                  
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
l = np.linspace(1,70,num = 5)
print(l)
#How to Create NumPy Arrays with Random Numbers
rnd= np.random.rand(4)
print(rnd)
print()
rnd1= np.random.rand(3,4)
print(rnd1)
print()
rnn = np.random.randn(5)
print(rnn)
print()
rn = np.random.randint(5,100,99)
print(rn)
rnf = np.random.ranf(5)
print(rnf)
#What is Data Type of NumPy Array?
# Integer Array
arr_int = np.array([1, 2, 3, 4, 5])
print("Integer Array:", arr_int)
print("dtype:", arr_int.dtype)
print()

# Float Array
arr_float = np.array([1.5, 2.5, 3.5, 4.5])
print("Float Array:", arr_float)
print("dtype:", arr_float.dtype)
print()

# String Array
arr_string = np.array(["Ali", "Ahmed", "Sara"])
print("String Array:", arr_string)
print("dtype:", arr_string.dtype)
print()

# Boolean Array
arr_bool = np.array([True, False, True, False])
print("Boolean Array:", arr_bool)
print("dtype:", arr_bool.dtype)
print()

# Complex Number Array
arr_complex = np.array([1+2j, 3+4j, 5+6j])
print("Complex Array:", arr_complex)
print("dtype:", arr_complex.dtype)
print()
# Custom int32 Data Type
arr_int32 = np.array([10, 20, 30], dtype=np.int32)
print("int32 Array:", arr_int32)
print("dtype:", arr_int32.dtype)
print()
# Custom float32 Data Type
arr_float32 = np.array([10, 20, 30], dtype=np.float32)
print("float32 Array:", arr_float32)
print("dtype:", arr_float32.dtype)
print()
# Convert Integer Array to Float
arr_convert = arr_int.astype(float)
print("Converted Array:", arr_convert)
print("dtype:", arr_convert.dtype)
#NumPy Arithmetic Operation
a = np.array([1,2,3,4,5,6])
b = np.array([1,2,3,4,5,6])
c = np.mod(a,b)
print(c)
a = np.array([1,2,3,4,5,6])
b = np.array([1,2,3,4,5,6])
c =a+b
print(c)

a = 10
b = 3
print(np.add(a, b))        # 13
print(np.subtract(a, b))   # 7
print(np.multiply(a, b))   # 30
print(np.divide(a, b))     # 3.3333333333333335
print(np.mod(a, b))        # 1
print(np.power(a, b))      # 1000
print(np.reciprocal(2.0))  # 0.5
#NumPy mathematical functions:
x = np.array([4, 16, 25, 9, 36])
print("Array:", x)
print(np.min(x))     
print(np.max(x))     
print(np.argmin(x)) 
print(np.sqrt(x))
print(np.sin(x))
print(np.cos(x))        
print(np.cumsum(x))
#Shape and Reshaping in NumPy Arrays 
v = np.array([[1,2,3,4],[1,2,3,4]])
print(v)
print()
print(v.shape)
var = np.array([1,2,3,4],ndim = 9)
print(var)
print()
print(var.shape)
x   = np.array([1,2,3,4,5])
arr = np.array([1, 2, 3, 4, 5, 6])

print("old Shape:", arr.shape)

arr2 = arr.reshape(2, 3)

print("new Shape:", arr2.shape)
#Indexing and Slicing In NumPy Arrays 
# 1D Array Operations
sil = np.array([1, 2, 3, 4, 5])
print(sil[3])        # Output: 4
Td = np.array([[7, 8, 9, 10], [1, 2, 3, 4]])
print(Td)            # Output: [[ 7  8  9 10] [ 1  2  3  4]]
print(Td.ndim)       # Output: 2
print(Td[1, 3])      # Output: 4
d3 = np.array([[[1,2],[6,2],[6,2]]])
print(d3)
print(d3.ndim)
print()
print(d3[0,2,1])

# 1D Array Operations
sil = np.array([1, 2, 3, 4, 5])
print(sil[0:])       # Output: [1 2 3 4 5]
print(sil[-3:-2])    # Output: [3]
# 2D Array Operations (Fixed row lengths)
Td = np.array([[7, 8, 9, 10], [1, 2, 3, 4]])
print(Td)            # Output: [[ 7  8  9 10] [ 1  2  3  4]]
print(Td.ndim)       # Output: 2
print(Td[1, 3])      # Output: 4
arr = np.arange(16)
print(arr)
print(arr[0:9:3])               #stay
#Copy vs Views Numpy Python Array 
var = np.array([1,2,3,4,5])
co = var.copy()
var[2]=40
print(var)
print(co)
var1 = np.array([1,2,3,4,5])
vi = var.view()
var[2]=40  
print(var)
print()
print(vi)
#Joining & Split NumPy Arrays Using (concatenate, stack, array_split )
j = np.array([1,23,4,5])
i = np.array([1,23,4,5])
arr = np.concatenate((j,i))
print("joining",arr)
var = np.array([[1,2],[1,2]])
vr = np.array([[1,2],[1,2]])
rr = np.concatenate((var,vr),axis=1)
r = np.concatenate((var,vr),axis=0)
print()
print("Marged",rr,r)
x = np.array([1,23,4,5])
y = np.array([1,23,4,5])
arr = np.stack((x,y))
print("joining",arr)
a = np.array([[1,2],[1,2]])
b = np.array([[1,2],[1,2]])
rr = np.stack((a,b),axis=1)
r = np.stack((a,b),axis=0)
print()
print("Marged",rr,r)
x = np.array([1,23,4,5])
y = np.array([1,23,4,5])
arr = np.hstack((x,y))
err = np.vstack((x,y))
irr = np.dstack((x,y))
print("joining",arr)
print("joining",irr)
print("joining",err)
a = np.array([[1,2],[1,2]])
b = np.array([[1,2],[1,2]])
rr = np.hstack((a,b))
e = np.vstack((a,b))
i = np.dstack((a,b))
print()
print("Marged",rr)
print("Marged",i)
print("Marged",e) 
v = np.array([1,23,4,5,1,23,4,5])
print(v)
new = np.array_split(v,3)
print()
print(new)
print(type(new))
print(new[0])
v1 = np.array([[1,23],[4,2],[4,5]])
print(v1)
new1 = np.array_split(v1,3)
new2 = np.array_split(v1,3,axis=0)
print()
print(new1)
print(type(new1))
print(new1[0])
print()
print(new2)
#Iterating NumPy Arrays - Learn Numpy Iteration with nditer Function 
# 1D Array
n = np.array([1,2,3,4,5])

print(n)
print()

for i in n:
    print(i)

# 2D Array
n1 = np.array([
    [1,2,3,4,5,6,7,8,9],
    [1,2,3,4,5,6,7,8,9]
])

print(n1)
print()

for e in n1:
    print(e)

print()

for f in n1:
    for j in f:
        print(j)

# 3D Array
array = np.array([
    [[1,2,3,4]],
    [[1,2,3,4]]
])

print(array)
print()

for i in array:
    for j in i:
        for k in j:
            print(k)
            array = np.array([
    [[1,2,3,4]],
    [[1,2,3,4]]
])

print(array)
print()

for ii in np.nditer(array):
    print(ii)
    array = np.array([
    [[1,2,3,4]],
    [[1,2,3,4]]
])

print(array)
print()

for i in np.nditer(array,flags=["buffered"],op_dtypes=["s"]):
    print(i)
    array = np.array([
    [[1, 2, 3, 4]],
    [[1, 2, 3, 4]]
])
print("\nIndexes and Values:")

for index, value in np.ndenumerate(array):
    print(f"{index} -> {value}")
#What are NumPy Arrays Functions
s = np.array([1, 2, 3, 4, 5, 6, 7, 8, 6, 1, 2, 3])

x = np.where(s == 6)
y = np.where((s % 2) == 0)

print("Indices of 6:")
print(x)

print("\nIndices of even numbers:")
print(y)

s1 = np.array([1, 2, 3, 4, 6, 7, 8, 9,10])

x1 = np.searchsorted(s1,5)
print(x1)
x2 = np.searchsorted(s1,5,side="right")
print(x2)
s1 = np.array([1, 2, 3, 4, 6, 7, 8, 9,10])
print(s1.dtype)
n=np.short(s1)
print(n)
print(n.dtype)
s1 = np.array([[1,2,3,4,51, 2, ],[ 4, 6, 7, 8, 9,10]])
print(s1.dtype)
n=np.short(s1)
print(n)
print(n.dtype)
fy = np.array(["s", "a", "s", "l", "p"])

f = [False, True, False, True, True]

new = fy[f]

print(new)
#What are NumPy Arrays Functions (Part 2)
h = np.array([1,2,3,7,5])
np.random.shuffle(h)
print(h)
u = np.array([1,2,3,7,5,5,9,8,1,1,2,4,3,7,10,1])

unique_values = np.unique(u)

print(unique_values) 
u = np.array([1,2,3,7,5,5,9,8,1,1,2,4,3,7,10,1])

unique_values = np.unique(u,return_index=True,return_counts=True)

print(unique_values)

u = np.array([1,2,3,7,5,5,9,8,1,1,2,4,3,7,10,1])

resize_values = np.resize(u, (4, 4))

print(resize_values)
import numpy as np

arr = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
a1 = arr.flatten()
a = arr.flatten(order="f")
print(a1)
print()
print(a)
print("revel",np.ravel(a,order="f"))
#What are NumPy Insert and Delete Arrays Functions
var = np.array([1, 2, 3, 4, 5])

new_arr = np.insert(var, 2, 100)

print("Original Array:", var)
print("New Array:", new_arr)
arr = np.array([[1, 2], 
                [3, 4]])
new_arr = np.insert(arr, 1, [9, 9], axis=0)
print(new_arr)
# Index 2 پر کالم شامل کریں
new_arr = np.insert(arr, 2, [5, 6], axis=1)
print(new_arr)
# 3D Array بنانا
arr_3d = np.array([
    [[1, 2], 
     [3, 4]],   # Matrix 0

    [[5, 6], 
     [7, 8]]    # Matrix 1
])
new_matrix = np.array([[9, 9], [9, 9]])
res_axis0 = np.insert(arr_3d, 1, new_matrix, axis=0)

print(res_axis0)
x = np.array([1,2,3,4,5,8])
print("array",x)
print()
new = np.append(x,[6,7])
print("new array",new)
x = np.array([10, 20, 30, 40, 50])

new = np.delete(x, 2)

print("Original:", x)
print("New:", new)
#The Concept of Matrix Numpy Arrays in Python
arr = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print("Matrix (2D Array):")
print(arr)
print()

# =========================
# 2. Shape of Matrix
# =========================
print("Shape of Matrix:")
print(arr.shape)
print()

# =========================
# 3. Type Check
# =========================
print("Type of arr:")
print(type(arr))
print()

# =========================
# 4. Matrix Addition
# =========================
a = np.array([
    [1, 2],
    [3, 4]
])

b = np.array([
    [5, 6],
    [7, 8]
])

print("Matrix A:")
print(a)
print()

print("Matrix B:")
print(b)
print()

print("Addition (A + B):")
print(a + b)
print()

# =========================
# 5. Element-wise Multiplication
# =========================
print("Element-wise Multiplication (A * B):")
print(a * b)
print()

# =========================
# 6. Matrix Multiplication (Dot Product)
# =========================
print("Matrix Multiplication (dot product):")
print(np.dot(a, b))
print()

# =========================
# 7. Reshaping Array
# =========================
x = np.array([1, 2, 3, 4, 5, 6])

print("Original Array:")
print(x)

print("Reshaped (2x3):")
print(x.reshape(2, 3))
print()

# =========================
# 8. Flatten Matrix
# =========================
print("Flatten Matrix:")
print(arr.flatten())
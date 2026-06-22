import pandas as pd
x = [1,2,3,4,5,6,7]
y = pd.Series(x,index=["a","b","c","d","f","g","h"],dtype="float",name="python")
print(y)
print(type(y))
#Basics of DataFrames in Pandas | Data Structure 
l= [1,2,3,4,5,7,8,9,10]
d_f=pd.DataFrame(l)
print(d_f,type(d_f))
print()
Dicit = {
    "a":[1,2,3,4,5,6,7,8,9,10],
    "s":[1,2,3,4,5,6,7,8,9,10],
    "d":[1,2,3,4,5,6,7,8,9,10],
    "e":[1,2,3,4,5,6,7,8,9,10],
}
x1 = pd.DataFrame
print(x1,type(x1))
print(x1["d"][2])
print(Dicit,columns=("a","e"),index=["a","b","c","d","e","f","g","h","i","j"])
print(x1,type(x1))
list_1=[[1,2,3,4,5,6,],[11,12,13,14,15,16]]
v2 = pd.DataFrame(list_1)
print(v2)
sr = {"s":pd.Series([1,2,3,4,5]),
   "r"   :pd.Series([1,2,3,4,5])}
var3 =  pd.DataFrame(sr)
print(var3)
# What are Arithmetic Operators in Python Pandas
D = pd.DataFrame({
    "a": [1, 2, 3, 4, 5],
    "b": [6, 7, 8, 9, 0]
})
D["c"] = D["a"] + D["b"]
print(D)
D = pd.DataFrame({
    "a": [1, 2, 3, 4, 5],
    "b": [6, 7, 8, 9, 0]
})
D["c"] = D["a"] - D["b"]

print(D)
D = pd.DataFrame({
    "a": [1, 2, 3, 4, 5],
    "b": [6, 7, 8, 9, 0]
})
D["c"] = D["a"] * D["b"]
print(D)
D = pd.DataFrame({
    "a": [1, 2, 3, 4, 5],
    "b": [6, 7, 8, 9, 0]
})

D["c"] = D["a"] / D["b"]

print(D)
var = pd.DataFrame({
    "a": [1, 2, 3, 4, 5, 6],
    "b": [1, 2, 3, 4, 5, 6]
})

print(var)
print()
var.insert(1,"python",var["a"])
var.insert(1,"python_1",[7,8,9,4,5,6,])
print(var)
df = pd.DataFrame({
    "Name": ["Ali", "Ahmed", "Sara"],
    "Age": [20, 22, 21]
})

df = df.drop("Age", axis=1)

print(df)
#Python Pandas CSV Files - Complete Tutorial | Pandas Tutorial
dis = {
    "a":[1,2,6,4,5],
    "s":[7,8,9,4,5],
    "d":[11,12,13,14,15]
}
d = pd.DataFrame(dis)
d.to_csv("text_new.csv")
d.to_csv("text_new.csv1",index=False)
d.to_csv("text_new.csv1",index=False,header=[1,2,3])
print(d)
#Read Python CSV files - with PANDAS |
csv_1 = pd.read_csv("C:\\Users\\Anwender\\Python Projects\\text_new.csv",nrows=3,) 
csv_1 = pd.read_csv("C:\\Users\\Anwender\\Python Projects\\text_new.csv",usecols=["s","a"]) 
print(csv_1)
v_1 = pd.read_csv(r"C:\Users\Anwender\Python Projects\text_new.csv", header=None)

csv_1.columns = [f"col{i}" for i in range(csv_1.shape[1])]

print(csv_1)
#Pandas Functions - Python CSV File Reading and Writing
csv_1 = pd.read_csv("C:\\Users\\Anwender\\Python Projects\\text_new.csv")
print(csv_1)
print(csv_1.index)
print(csv_1.columns)
print(csv_1.describe())
print(csv_1.head())
print(csv_1.tail())
print("index_file",csv_1[0:3])
print(type(csv_1))
csv_1.index.array
print(csv_1.index.array)
print(csv_1.to_numpy())
import numpy as np
arr = np.array(csv_1)
print(arr)
x=csv_1.sort_index(axis=0,ascending=False)
print(x)
y=csv_1.loc[0,"a"]=["python"]
print(y)
# How to Merge and Concat DataFrames

m = pd.DataFrame({
    "a": [1, 2, 3, 4],
    "b": [4, 5, 6, 7]
})
c = pd.DataFrame({
    "a": [1, 2, 3, 4],
    "c": [41, 51, 61, 17]
})

result = pd.merge(m, c, on="a")
result_1= pd.merge(m, c, )
result_2= pd.merge(m, c, how="left")
result_3= pd.merge(m, c, how="right")
result_4= pd.merge(m, c, how="outer",indicator=True)
print(result)
print()
print(result_1)
print()
print(result_2)
print()
print(result_3)
print()
print(result_4)
m = pd.DataFrame({
    "a": [1, 2, 3, 4],
    "b": [4, 5, 6, 7]
})

c = pd.DataFrame({
    "a": [1, 2, 3, 4],
    "b": [41, 51, 61, 17]
})

result_41= pd.merge(
    m, c, how="outer",indicator=True,left_index=True,right=True,suffixes=("names,","python"))

print(result_41)
s = pd.Series([1,2,3,4,5])
s1=pd.Series([1,2,3,4,5])
a = pd.concat([s,s1])
print(a)
d = pd.DataFrame({
    "a": [1, 2, 3, 4],
    "b": [4, 5, 6, 7]
})

c = pd.DataFrame({
    "a": [1, 2, 3, 4],
    "c": [41, 51, 61, 17]
})
print(pd.concat([d,c],axis=0,join="inner",keys=["d","s"]))
# Pandas GroupBy - Guide to Grouping Data in Python Pandas
# Create DataFrame
var = pd.DataFrame({
    "Name": ["a", "b", "c", "d", "a", "b", "a", "b", "a", "c", "c", "d"],
    "S_1":  [12, 13, 14, 12, 13, 14, 15, 23, 25, 16, 10, 34],
    "S_2":  [23, 24, 25, 26, 27, 28, 29, 30, 25, 34, 35, 56]
})

# Display DataFrame
print(var)
new_var=var.groupby("Names")
for x ,y in new_var:
    print(x)
    print(y)
    print()
    print(new_var.mean())
    print(new_var.max())
    li = list(new_var)
    print(li)
    # How to Join and Append DataFrames
vr1 = pd.DataFrame(
    {"A": [1, 2, 3, 4], "B": [11, 12, 13, 14]},
    index=["a", "b", "c", "d"]
)

vr2 = pd.DataFrame(
    {"C": [10, 20], "D": [11, 22]},
    index=["a", "b"]
)

# join + print result
result = vr1.join(vr2,how="outer")
print(result)

# How to Join and Append DataFrames
var1 = pd.DataFrame(
    {"A": [1, 2, 3, 4], "B": [11, 12, 13, 14]},
    index=["a", "b", "c", "d"]
)

var2 = pd.DataFrame(
    {"A": [10, 20], "B": [11, 22]},
    index=["a", "b"]
)

# Join with suffixes
result = var1.join(
    var2,
    how="outer",
    lsuffix="_left",
    rsuffix="_right"
)

print(result)
#Python Pandas Tutorial - Pivot Table and Melt Function - Explained

data = {
    "Name": ["Ali", "Ali", "Sara", "Sara"],
    "Subject": ["Math", "Science", "Math", "Science"],
    "Marks": [80, 90, 85, 95]
}

df = pd.DataFrame(data)

print(df)

pivot = df.pivot_table(
    index="Name",
    columns="Subject",
    values="Marks"
)

print(pivot)


df = pd.DataFrame({
    "Name": ["Ali", "Sara"],
    "Math": [80, 85],
    "Science": [90, 95]
})

print(df)

melt_df = pd.melt(
    df,
    id_vars=["Name"]
)

print(melt_df)
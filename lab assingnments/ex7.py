#how to use numpy array module - Tips
#Two dimensional array(matrix) can be given by listing the rows of the array:
import numpy as np
TwoDmatrix=np.array([[1,2,3],[4,5,6]])
print(TwoDmatrix)

#Dimensional array(matrix) can be given by listing the rows of the array:

oneDmatrix=np.array([1,2,3])
print(oneDmatrix)

# Three dimensional array/matrix can be described as a list of lists of lists:
threeDMatrix = np.array([[[1,2], [3,4]], [[5,6], [7,8]]])
print(threeDMatrix)

#create 5 dimentional identity matrix
fiveid=np.eye(5,dtype=int)
print(fiveid)

# Program 1: convert a list of numeric value into a one-dimensional NumPy
# array. NumPy is a module
import numpy as np
list1 = [95.20, 213.42, 300, 26.45, 503, 435]
print("List :",list1)
converted_array = np.array(list1)
print("One-dimensional NumPy array: ", converted_array)

import numpy as np
x = np.arange(10, 19).reshape(3,3)
print(x)

import numpy as np
x = np.array([1,2,3], dtype=np.float64)
print("Size of the array: ", x.size)
print("Length of one array element in bytes: ", x.itemsize)
print("Total bytes consumed by the elements of the array: ",x.nbytes)

import numpy as np
array1 = np.array([0, 10, 20, 40, 60])
print("Array1: ",array1)
array2 = [0, 40]
print("Array2: ",array2)
print("Compare each element of array1 and array2")
print(np.in1d(array1, array2))

x=np.array([[0,10.5,20.3,45.2,60.4,30.2],[20.5,30.6,40.9,50,2,56.9]])
print('first array:')
print(x)
print("Values bigger than 20 =", x[x>20])
print("Their indices are ", np.nonzero(x > 20))
x=np.array([[2,4,6],[7,8,9]],np.int32)
print(x.itemsize)
print(type(x))
print(x.shape)
print(x.dtype)

a=np.array([[0,8,6],[3,5,40]])
b=np.array([[4,7,5,],[8,2,9]])
c=np.concatenate((a,b),1)
print(c)
c=np.concatenate((a,b))
print(c)
c=np.concatenate((a,b),None)
print(c)
x=np.arange(16).reshape((4,4))
print("Original array:",x)
print(np.hsplit(x,[2,6]))

x=np.arange(12).reshape(3,4)
print("Original array elements:")
print(x)
print("Above array in small chuncks:")
for a in np.nditer(x,flags=['external_loop'], order='F'):
     print(a)

a1=np.array([1,2,3,4])
a2=np.array(['Red','Green','White','Orange'])
a3=np.array([12.20,15,20,40])
result= np.core.records.fromarrays([a1, a2, a3],names='a,b,c')
print(result[0])
print(result[1])
print(result[2])
x=np.array([10,20,30,50,66,50,20,11,20],float)
print(x)
print("put 0 and 40 in first and fifth position of the above array")
y=np.array([0,40,60],float)
x.put([0, 4], y)
print("Array x, after putting two values:")
print(x)

# """
# output

# [[1 2 3] 
#  [4 5 6]]
# [1 2 3]     
# [[[1 2]     
#   [3 4]]    

#  [[5 6]     
#   [7 8]]]   
# [[1 0 0 0 0]
#  [0 1 0 0 0]
#  [0 0 1 0 0]
#  [0 0 0 1 0]
#  [0 0 0 0 1]]
# List : [95.2, 213.42, 300, 26.45, 503, 435]
# One-dimensional NumPy array:  [ 95.2  213.42 300.    26.45 503.   435.  ]
# [[10 11 12]
#  [13 14 15]
#  [16 17 18]]
# Size of the array:  3
# Length of one array element in bytes:  8
# Total bytes consumed by the elements of the array:  24
# Array1:  [ 0 10 20 40 60]
# Array2:  [0, 40]
# Compare each element of array1 and array2
# [ True False False  True False]
# first array:
# [[ 0.  10.5 20.3 45.2 60.4 30.2]
#  [20.5 30.6 40.9 50.   2.  56.9]]
# Values bigger than 20 = [20.3 45.2 60.4 30.2 20.5 30.6 40.9 50.  56.9]
# Their indices are  (array([0, 0, 0, 0, 1, 1, 1, 1, 1], dtype=int64), array([2, 3, 4, 5, 0, 1, 2, 3, 5], dtype=int64))
# 4
# <class 'numpy.ndarray'>
# (2, 3)
# int32
# [[ 0  8  6  4  7  5]
#  [ 3  5 40  8  2  9]]
# [[ 0  8  6]
#  [ 3  5 40]
#  [ 4  7  5]
#  [ 8  2  9]]
# [ 0  8  6  3  5 40  4  7  5  8  2  9]
# Original array: [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]
#  [12 13 14 15]]
# [array([[ 0,  1],
#        [ 4,  5],
#        [ 8,  9],
#        [12, 13]]), array([[ 2,  3],
#        [ 6,  7],
#        [10, 11],
#        [14, 15]]), array([], shape=(4, 0), dtype=int32)]
# Original array elements:
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]
# Above array in small chuncks:
# [0 4 8]
# [1 5 9]
# [ 2  6 10]
# [ 3  7 11]
# (1, 'Red', 12.2)
# (2, 'Green', 15.)
# (3, 'White', 20.)
# [10. 20. 30. 50. 66. 50. 20. 11. 20.]
# put 0 and 40 in first and fifth position of the above array
# Array x, after putting two values:
# [ 0. 20. 30. 50. 40. 50. 20. 11. 20.]

# """
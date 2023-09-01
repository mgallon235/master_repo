import numpy as np
import pandas as pd


# Creating a numpy array
num_list = [1,2,3,4,5,6,7]
type(num_list)

# Transform list to a numpy array
num_array = np.array(num_list)

# Check the type of the values inside our numpy array
num_array.dtype

# Creating a multidimensional array  in Numpy using a list of lists:
row1 = [1,2,3]
row2 = [4,5,6]
row3 = [7,8,9]

num_2d = np.array([row1,row2,row3])
print(num_2d)
# Show the shape of the matrix
print(num_2d.shape)


# Using the arrange method to create an array:
nums_arr = np.arange(5,10)
# creates a numpy array  with values  between 5 and 10 (in order) and do not include the start or end input.
print(nums_arr)

# You can also include a  step parameter which defines the distance between values
nums_arr_2 = np.arange(5,10,2)
print(nums_arr_2)

# Using the ones method: create a numpy array of all ones.
ones_arr = np.ones(6)
print(ones_arr)

# You can also create a matrix 0f 2-dimensional object by passing 2 parameters (row, cols) within brackets
ones_arr_3 = np.ones((3,3))
print(ones_arr_3)

# Using zeros method : creates an  array of zeros only.

zero_arr = np.zeros(10)
print(zero_arr)

# Same as with ones method, we can  create a matrix defining the  values for the rows and cols
zero_arr_3 = np.zeros((3,3))
zero_arr_3.shape
print(zero_arr_3)

## Using Eyes method (IDENTITY MATRIX) - creates a two dimiensional array. Given that identity matrices are always square 
## we only need to pass 2 parameter that defines the n by n matrix.

identity_arr = np.eye(3)
print(identity_arr)

''' ------------------------------------------- '''

# Generating random arrays using numpy

# random.rand() - creates random array with uniform (between 0 and 1) distribution, also creates a 2-dimensional 
# we need to specify the row and column
uniform_random = np.random.rand(4,5)

# We can use a  for loop to print the 2-dimensional array:
for i in uniform_random:
    print(i)

# random.randn() - creates random array with normal distribution, also creates a 2-dimensional. we need tospecify n and m
normal_arr = np.random.randn(4,5)

# print using a for loop:
for i in normal_arr:
    print(i)

# random.randint()  -  creates random array  using random integers between a certain range. 3 parametes:
# lower-bound
# upper-bound 
# number of random integers to generate
integer_rand = np.random.randint(30,45,10)

print(integer_rand)

for i in integer_rand:
    print(i)

## How to  know how many dimensions your array has:
integer_rand.ndim # 1 dim (vector)
normal_arr.ndim # 2 dim (matrix)
# Show the shape - in case of 1   dimensional will tell you the number of  observations - for a 2-dim the row  x cols
integer_rand.shape
normal_arr.shape

# To  create a matrix from the random.randint() - we need to specify the num rows and columns (size) instead of numb of observations
int_matrix = np.random.randint(30,45, size =(3,3))
print(int_matrix)

for i in int_matrix:
    print(i)

# What happens if we want to print each value within all vectors as 
for rows in  int_matrix:
    for columns in rows:
        print(columns)

'''----------------------------------------------'''

## Adding items in a Numpy array

#  You can use the append() method. the append() method returns a new array that contains newly added items appended  at the 
# end of the original array

array_test = np.random.randint(1,10, 5)

print(array_test)

# Now lets add a new value to our array_test:

extented_arr = np.append(array_test,[0,0,1,0,0])
print(extented_arr)


'''-------------------------'''

## Add items in a 2-dimensional Numpy array. You need to specify whether you want to add the new item 
# as a row or as a column. To do so , you can take the help of the axis attribute of the append method.

# Lets first create a 3x3 matrix of all zeros
test_zero = np.zeros((3,3))

print(test_zero)

# A. Add a new  row to 3x3 matrix
### You need to pass the original array in the form of a row vector and the  axis attribute to the append().
### To add the 
row_s = [0,0,105] # in order to be able to add this list we need to put inside another set of square brackets (2-dimension)
extended_zero = np.append(test_zero,[row_s], axis = 0)

print(extended_zero)

# B. Add a new column
extended_zero_c = np.append(extended_zero,[[1],[0],[0],[0]], axis = 1)

for i in extended_zero_c:
    print(i)

print(extended_zero_c.shape)

'''-----------------------------------------'''

# do some inner product with matrices/ (vectors)

xs= np.array([[1],[0],[-1]])
ys = np.array([[3],[2],[0]])

# first multiplication

xsys = np.dot(np.transpose(xs),ys)

xsys

'''------------------------------------------'''

# Calculating the norm of a vector

xn = np.array([[1],[0],[-1]])
xn_norm = np.linalg.norm(xn)

xn_norm

'''------------------------------------------'''

W = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(W)

xe= np.array([[2],[-1],[1]])

z = np.dot(xe.T,np.dot(W,xe))

z


'''----------------------------------------'''

# Python code to compute the matrix inverse

xn = np.array([[1,3],[-2,7],[0,1]])
xtx = np.dot(xn.T,xn)
xtxinv = np.linalg.inv(xtx)

print(xtxinv)

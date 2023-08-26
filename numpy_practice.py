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

# Random.rand() - creates random array with uniform (between 0 and 1) distribution, also creates a 2-dimensional 
# we need to specify the row and column
uniform_random = np.random.rand(4,5)

# We can use a  for loop to print the 2-dimensional array:
for i in uniform_random:
    print(i)
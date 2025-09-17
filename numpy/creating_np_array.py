import numpy as np

# creating a rank 1 Array
arr = np.array([1,2,3])
print(arr)

# creating a rank 2 Array
arr = np.array([[1,2,3],
                [4,5,6]])
print(arr)

# creating a rank 3 Array

arr = np.array(
    [
        [[1,2,3], [4,5,6]],
        [[1,2,3], [2,3,4]]
    ]
)
print("########################")
print(arr)

# Creating an array from tuple
arr = np.array((1,2,3))
print(arr)


 
arr = np.array([[-1, 2, 0, 4],
                [4, -0.5, 6, 0],
                [2.6, 0, 7, 8],
                [3, -7, 4, 2.0]])

# Printing a range of Array
# with the use of slicing method
arr2 = arr[:2, ::2]
print ("first 2 rows and alternate columns(0 and 2):\n", arr2)
 
# Printing elements at
# specific Indices
arr3 = arr[[1, 1, 0, 3], 
            [3, 2, 1, 0]]
print ("\nElements at indices (1, 3), "
    "(1, 2), (0, 1), (3, 0):\n", arr3)
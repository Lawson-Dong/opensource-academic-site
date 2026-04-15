import numpy as np  # Give np as a short name, everyone does this

# Create the first NumPy array
my_first_array = np.array([1, 2, 3, 4, 5])

print(my_first_array)
# Output: [1 2 3 4 5]

print(type(my_first_array))
# Output: <class 'numpy.ndarray'>


## The array is a list of numbers, but it is not a list. It is a NumPy array, which is a different type of data structure. The array has many more features than a list, such as the ability to perform mathematical operations on the entire array at once, and the ability to store multi-dimensional data.
## The comparison between a list and a NumPy array 

# Standard list approach
python_list = [1, 2, 3, 4, 5]
# Want to multiply each number by 2? A Python list would fail, requiring a loop
# doubled_list = python_list * 2  # This copies the list, not mathematical multiplication!

# NumPy array approach
numpy_arr = np.array([1, 2, 3, 4, 5])
doubled_arr = numpy_arr * 2

print(doubled_arr)
# Output: [ 2  4  6  8 10]  — Completed instantly, no loop needed!
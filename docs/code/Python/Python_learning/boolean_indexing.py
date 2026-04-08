import numpy as np



# a simple example of boolean indexing
arr = np.array([0.2, -0.5, 0.8, 1.2, 0.3, -0.1])
mask = (arr > 0) & (arr < 1)
print(mask)        # [ True False  True False  True False]
print(arr[mask])   # [0.2 0.8 0.3]
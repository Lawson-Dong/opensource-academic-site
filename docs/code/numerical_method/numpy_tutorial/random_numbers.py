import numpy as np
import matplotlib.pyplot as plt

# Correct usage examples
randint_data = np.random.randint(0, 50, 1000)    # 1000 integers from 0-49
rand_data = np.random.rand(1000)                 # 1000 floats in [0,1)
randn_data = np.random.randn(1000)               # 1000 normal distribution values
choice_data = np.random.choice(50, 50, replace=False)   # 0-49 random permutation

# Distribution characteristics:
# randint: probability of each integer ≈ 1/50 (uniform)
# rand: values concentrated between 0-1 (uniform)
# randn: 68% of data within [-1, 1], 95% within [-2, 2]
# choice(replace=False): each number appears exactly once, just random order.
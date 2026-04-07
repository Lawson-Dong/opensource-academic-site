import numpy as np
import matplotlib.pyplot as plt


data = {'a': np.arange(50),
        'c': np.random.randint(0, 50, 50),
        'd': np.random.randn(50)}
data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 100

plt.scatter('a',  #x-axis
            'b',  #y-axis 
            c='c',  #color of points
            s='d',  #size of points 
            data=data) #data source for the above parameters (can be a dictionary in this case)
plt.xlabel('entry a')
plt.ylabel('entry b')
plt.show()

#  plt.scatter function

    

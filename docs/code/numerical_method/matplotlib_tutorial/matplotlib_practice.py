import numpy as np
import matplotlib.pyplot as plt

#plt.plot([1,2,3,4,5])
#plt.plot([1,2,3,4,5], [1,4,9,16,25], "ro")
 
 
# evenly sampled time at 200ms intervals

t = np.arange(0., 5., 0.2)
t_exp = np.exp(t)
plt.plot(t, t, 'r--',t, t**2, 'ro-', t, t_exp, 'bs-')

plt.ylabel('some numbers')
plt.xlabel('some numbers')
plt.title('A simple plot')
plt.show()


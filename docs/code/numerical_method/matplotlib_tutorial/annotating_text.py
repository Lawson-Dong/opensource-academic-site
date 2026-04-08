import numpy as np
import matplotlib.pyplot as plt

ax = plt.subplot()

t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2*np.pi*t)
line, = plt.plot(t, s, lw=2)

plt.annotate('local max',                                     # text to display (label)
             xy=(2, 1),                                       # point that the arrow points to (annotated position)
             xytext=(3, 1.5),                                 # position where the text is placed
             arrowprops=dict(facecolor='black', shrink=0.05)  # arrow properties
             )

plt.ylim(-2, 2)
plt.show()
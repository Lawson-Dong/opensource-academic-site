import numpy as np
import matplotlib.pyplot as plt

mu, sigma = 100, 15
epsilon = np.random.randn(10000)

x = mu + sigma * epsilon

# the histogram of the data
n, bins, patches = plt.hist(x, 50, density=True, facecolor='g', alpha=0.75)


plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title('Histogram of IQ')
plt.text(60,                             #X-coordinate of the text
         0.025,                          #Y-coordinate of the text
         r'$\mu=100,\ \sigma=15$')       #Text to display, can include LaTeX formatted math
plt.axis([40, 160, 0, 0.03])
plt.grid(True)
plt.show()

# 0.025 can be written as .025 or 2.5e-2, but 0.025 is more concise and easier to read.
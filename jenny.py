import math
import numpy as np
import matplotlib.pyplot as plt

def L(x):
    #return 1.277 + 0.000167*x
    return -0.0545 -0.0005*x

def P(x):
    return 1/(1 + np.exp(-L(x)))

#x = np.arange(0, 1000, 1)
print((P(300) - P(100))*100)

#plt.plot(x, P(x))
#plt.show()
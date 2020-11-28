import matplotlib.pyplot as plt
import numpy as np

xvals = np.linspace( -5, 5, 500 )
yvals = -2*xvals*xvals + 8*xvals - 8

plt.plot( xvals, yvals, 'k-')
plt.savefig("quad.png")

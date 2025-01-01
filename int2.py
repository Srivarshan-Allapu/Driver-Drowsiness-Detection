import numpy as np
import matplotlib.pyplot as plt
x = np.random.randn(100)
yl = x * 5 + 9
y2 = -5 * x
y3 = np.random.randn(100)
plt.rcParams.update({'figure.figsize': (10, 8), 'figure.dpi': 100})
plt.scatter(x, yl, label=f'y1, Correlation = {np.round(np.corrcoef(x,yl)[0,1], 2)}')
plt.scatter(x, y2, label='y2, Correlation = {np.round(np.corrcoef(x,y2)[0,1], 2)}')
plt.scatter(x, y3, label='y3, Correlation = {np.round(np.corrcoef(x,y3)[0,1], 2)}')
plt.title('Scatterplot and Correlations')
plt.legend()
plt.show()

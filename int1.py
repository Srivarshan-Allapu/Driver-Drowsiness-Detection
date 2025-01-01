from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sb
data = np.arange(1, 10, 0.01)
pdf = norm.pdf(data, loc=5.3, scale=1)
sb.set_style('whitegrid') 
sb.lineplot(x=data, y=pdf, color='black')
plt.xlabel('Heights') 
plt.ylabel('Probability Density')
plt.show()

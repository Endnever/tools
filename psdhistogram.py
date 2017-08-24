# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 11:56:02 2017

@author: mtp16sr
"""
import pandas as pd
from scipy import stats
import numpy as np
from matplotlib import pyplot as plt

targetdata=pd.read_csv("micro1.csv")
df=pd.DataFrame(targetdata)
histvs=df['area']

n, bins, patches = plt.hist(histvs, bins=25, normed=True) # Plot histogram

shape, loc, scale = stats.lognorm.fit(histvs, floc=0) # Fit a curve to the variates
mu = np.log(scale) # Mean of log(X)
sigma = shape # Standard deviation of log(X)
M = np.exp(mu) # Geometric mean == median
s = np.exp(sigma) # Geometric standard deviation

# Plot figure of results
x = np.linspace(histvs.min(), histvs.max(), num=400)
plt.plot(x, stats.lognorm.pdf(x, shape, loc=0, scale=scale), 'r', linewidth=3) # Plot fitted curve
ax = plt.gca() # Get axis handle for text positioning
txt = plt.text(0.9, 0.9, 'M = %.2f\ns = %.2f' % (M, s), horizontalalignment='right', 
                size='large', verticalalignment='top', transform=ax.transAxes)
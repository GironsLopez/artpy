# -*- coding: utf-8 -*-
"""
Created on Mon May 23 17:30:23 2016

SUNSET BEHIND THE MOUNTAINS

@author: marc.girons
"""

import os
import numpy as np
import matplotlib.pyplot as plt

path = os.pardir + '\\img\\'

mean = [0, 10, 0]
cov = [[1, 0, 0], [1, 1, 1], [1, 0, 0]]  # diagonal covariance
x, y, z = np.random.multivariate_normal(mean, cov, 1000).T

# get the closer mountains on top
sort = np.argsort(z)[::-1]

fig = plt.figure(figsize=(8, 4))

ax = plt.subplot(111)
for i in sort:
    # the furthest and highest point represents the sun
    if i == sort[0]:
        ax.scatter(x[i], y[i], c=z[i], cmap='plasma', marker='o',
                   edgecolor='none', s=2000, vmin=z.min(), vmax=z.max())
    else:
        # get mountain height
        d = np.random.random() * 1000

        # get the shadows of the mountains
        xxs = np.arange(0.1, 1.0, 0.1)
        yys = np.arange(0.05, 0.30, 0.05)
        dds = np.arange(0.1, 1.1, 0.2)[::-1]
        for xx, yy, dd in zip(xxs, yys, dds):
            ax.scatter(x[i]-xx, y[i]-yy-0.0005*d, c=z[i], marker='_',
                       cmap='plasma', edgecolor='none', s=d*dd,
                       vmin=z.min(), vmax=z.max())

        # plot the mountains
        ax.scatter(x[i], y[i], c=z[i], marker='^', cmap='plasma',
                   edgecolor='none', s=d, vmin=z.min(), vmax=z.max())

        # mountains above 950 m a.s.l. have snow
        if d > 950:
            ax.scatter(x[i], y[i]+0.35, c='w', marker='^',
                       edgecolor='none', s=25)

plt.axis('off')
plt.savefig(path + 'sunset.png', transparent=True, format='png')

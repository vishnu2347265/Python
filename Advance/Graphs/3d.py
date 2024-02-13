import numpy as np
from numpy import linspace
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from mpl_toolkits.mplot3d import Axes3D
from scipy import signal
from mpl_toolkits.basemap import Basemap
import ipympl
df = pd.read_csv('Iris.csv')
setosa=df[df['Species']=='Iris-setosa']
versicolor=df[df['Species']=='Iris-versicolor']
virginica=df[df['Species']=='Iris-virginica']
plt.rcParams['font.size']=10
fig=plt.figure()
ax=fig.add_subplot(111, projection='3d')
ax.bar(setosa['Id'],setosa['PetalWidthCm'], zs=1, zdir='x', color='red', alpha=0.8)
ax.bar(versicolor['Id'],versicolor['PetalWidthCm'], zs=2, zdir='x', color='green', alpha=0.8)
ax.bar(virginica['Id'],virginica['PetalWidthCm'], zs=3, zdir='x', color='blue', alpha=0.8)
ax.set_xlabel('Species')
ax.set_ylabel('Id')
ax.set_zlabel('PetalWidthCm')
plt.show()
from matplotlib import figure
import numpy as np
from numpy import linspace
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from mpl_toolkits.mplot3d import Axes3D
from scipy import signal
from mpl_toolkits.basemap import Basemap
import ipympl





data=pd.read_csv("D:\Progrmming\Python\Advance\Lab1\Q8_MortalityDataset.csv")
alive = data[data['MORT'] == 'alive']
dead = data[data['MORT']=='dead']

fig =  plt.figure()


ax1 = fig.add_subplot(223,projection='3d')
ax1.scatter(alive['HEIGHT'], alive['WEIGHT'], alive['AGE'], c='b', marker='o', label='Alive')
ax1.set_title('3D scatter plot')
ax1.set_xlabel('Height')
ax1.set_ylabel('Weight')
ax1.set_zlabel('Age')
ax1.legend()
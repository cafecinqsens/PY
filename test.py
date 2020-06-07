import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import datetime as dt

birdata = pd.read_csv('bird_tracking.csv')

speed = birdata.speed_2d[birdata.bird_name == 'Eric']

speed = np.array(speed)

np.isnan(speed)

print(len(np.isnan(speed)))

'''
def getnan(s):
    for i, n in enumerate(s):
        if np.isnan(n):
            return i
ind = getnan(speed)

print(ind)
'''
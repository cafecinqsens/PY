'''
AI기초통계
13장 빅데이터 분석 과제
교안 237페이지 하단

20. 5. 17.

차재관 작성
'''

import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.pyplot as plt
import pandas as pd
from scipy.spatial import distance
import numpy as np

proj = ccrs.Mercator()
plt.figure(figsize=(10, 10))
ax = plt.axes(projection = proj)
ax.set_extent((-25.0, 20.0, 52.0, 10.0))
ax.add_feature(cfeature.LAND)
ax.add_feature(cfeature.OCEAN)
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.BORDERS, linestyle=':')


bird_dist = {} #사전형으로 저장
distlist = []

def euc(a, b):
    return distance.euclidean(a, b) 
birddata = pd.read_csv('bird_tracking.csv')
bird_names = pd.unique(birddata.bird_name)

start = 0 # start 변수 선언 0을 저장
dest = 0
count = 0

for bird_name in bird_names:
    ix = birddata['bird_name'] == bird_name # 각각의 bird_name 원소에 데이터 분류
    x, y = birddata.longitude[ix], birddata.latitude[ix]
    longest = 0 # longest 변수를 선언하고 0을 저장 

    i = [x[start], y[start]]

    for ind in range(len(x)-1):
        j = [x[start+ind+1], y[start+ind+1]]

        newlength = euc(i, j)
        distlist.append(newlength) 
        if(euc(i, j) > longest):
            longest = newlength
            bird_distkm = longest * (40000 / 360) #4만 킬로를 360도로 나눔
    bird_dist[bird_names[count]] = bird_distkm
    count = count + 1 
    start = start + len(x) 
    dest = dest + len(x)



print(bird_dist)



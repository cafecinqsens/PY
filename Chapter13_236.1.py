'''
AI기초통계
13장 빅데이터 분석 과제
교안 236페이지 상단

20. 5. 17.

차재관 작성
'''

import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.pyplot as plt
import pandas as pd
from scipy.spatial import distance
# scipy에서 spatial 패키지 중 distance 모듈을 가져오기

proj = ccrs.Mercator()
plt.figure(figsize=(10, 10))
ax = plt.axes(projection = proj)
ax.set_extent((-25.0, 20.0, 52.0, 10.0))
ax.add_feature(cfeature.LAND)
ax.add_feature(cfeature.OCEAN)
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.BORDERS, linestyle=':')

longest = 0

distlist = []

def euc(a, b):
    return distance.euclidean(a, b) # 유클리드 거리: 두 점을 계산할 때 사용
birddata = pd.read_csv('bird_tracking.csv')

ix = birddata['bird_name'] == 'Eric'
x, y = birddata.longitude[ix], birddata.latitude[ix]

i = [x[0], y[0]]

for ind in range(len(x)-1):
    j = [x[ind+1], y[ind+1]]

    newlength = euc(i, j)
    distlist.append(newlength) # distlist 리스트에 newlength를 하나씩 저장
    if(euc(i, j) > longest): # 만약에 거리가 longest보다 크다면
        longest = newlength  # newlength를 longest에 저장
print('Longest=', longest)
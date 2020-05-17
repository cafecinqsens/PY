'''
AI기초통계
13장 빅데이터 분석 과제
교안 234페이지~235페이지 상단

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

def euc(a, b):
    return distance.euclidean(a, b) # 유클리드 거리: 두 점을 계산할 때 사용

birddata = pd.read_csv('bird_tracking.csv')
bird_names = pd.unique(birddata.bird_name)

sindex = 15000 # 시작 인덱스
eindex = 18300 # 끝 인덱스

ix = birddata['bird_name'] == 'Eric'
x, y = birddata.longitude[ix], birddata.latitude[ix]

i = [x[sindex], y[sindex]]
j = [x[eindex], y[eindex]]


ax.plot(x[sindex:eindex], y[sindex:eindex], '.', transform=ccrs.Geodetic())
print('Eric', euc(i, j))

ix = birddata['bird_name'] == 'Nico'
x, y = birddata.longitude[ix], birddata.latitude[ix]

start = len(x)
dest = len(y)

i = [x[start+sindex], y[start+sindex]]
j = [x[dest+eindex], y[dest+eindex]]

ax.plot(x[sindex:eindex], y[sindex:eindex], '.', transform=ccrs.Geodetic())
print('Nico', euc(i, j))

ix = birddata['bird_name'] == 'Sanne'
x, y = birddata.longitude[ix], birddata.latitude[ix]

start = start + len(x)
dest = dest + len(y)

i = [x[start+sindex], y[start+sindex]]
j = [x[dest+eindex], y[dest+eindex]]

ax.plot(x[sindex:eindex], y[sindex:eindex], '.', transform=ccrs.Geodetic())
print('Sanne', euc(i, j))
plt.show()
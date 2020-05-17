'''
AI기초통계
13장 빅데이터 분석 과제
교안 233페이지 하단

20. 5. 17.

차재관 작성
'''

import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.pyplot as plt
import pandas as pd

proj = ccrs.Mercator()
plt.figure(figsize=(10, 10))
ax = plt.axes(projection = proj)
ax.set_extent((-25.0, 20.0, 52.0, 10.0))
ax.add_feature(cfeature.LAND)
ax.add_feature(cfeature.OCEAN)
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.BORDERS, linestyle=':')

birddata = pd.read_csv('bird_tracking.csv')
bird_names = pd.unique(birddata.bird_name)
ix = birddata['bird_name'] == 'Eric'
x, y = birddata.longitude[ix], birddata.latitude[ix]
ax.plot(x[0:17000], y[0:17000], '.', transform=ccrs.Geodetic())
ax.plot(x[17001:18600], y[17001:18600], '.', transform=ccrs.Geodetic())

plt.show()
'''
AI기초통계
13장 빅데이터 분석 과제
교안 232페이지 상단

20. 5. 17.

차재관 작성
'''

import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.pyplot as plt
import pandas as pd

proj = ccrs.Mercator()
plt.figure(figsize=(7, 7))
# 사이즈를 7, 7로 변경
ax = plt.axes(projection = proj)
ax.set_extent((-25.0, 20.0, 52.0, 10.0))
ax.add_feature(cfeature.LAND)
ax.add_feature(cfeature.OCEAN)
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.BORDERS, linestyle=':')

birddata = pd.read_csv('bird_tracking.csv')
x, y = birddata.longitude, birddata.latitude
# 전체 새의 데이터 경도, 위도를 받음
ax.plot(x, y, '.', transform=ccrs.Geodetic())
# 교안과 다름, 확인 필요

plt.show()
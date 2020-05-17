'''
AI기초통계
13장 빅데이터 분석 과제
교안 231페이지 하단

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
# 경로는 자신의 컴퓨터 환경에 따라 다름
# 파일명만 쓸려면 같은 폴더 내에 위치하고 있어야 함

bird_names = pd.unique(birddata.bird_name)
# 새 데이터에 저장된 새 이름만 저장


for name in bird_names:
    ix = birddata['bird_name'] == name
    x, y = birddata.longitude[ix], birddata.latitude[ix]
    # longitude -> 경도, latitude -> 위도

    ax.plot(x, y, '.', transform=ccrs.Geodetic(), label=name)
    # transform의 Geodetic -> 지구를 입체적으로 표현
plt.legend(loc='upper left')
# 범례 위치
plt.show()
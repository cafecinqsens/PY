'''
AI기초통계
13장 빅데이터 분석 과제
교안 232페이지 하단

20. 5. 17.

차재관 작성
'''

import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.pyplot as plt
import pandas as pd

plt.figure(figsize=(7, 7))

birddata = pd.read_csv('bird_tracking.csv')
ix = birddata.bird_name == 'Eric'
# Eric인 데이터만 추출

x, y = birddata.longitude[ix], birddata.latitude[ix]
plt.plot(x, y, '.')

plt.show()

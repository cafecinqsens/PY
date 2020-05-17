'''
AI기초통계
13장 빅데이터 분석 과제
교안 230페이지 하단

20. 5. 17.

차재관 작성
'''


import cartopy.crs as ccrs

# == 카토피 설치법  ==
# VSCODE 하단 터미널 창에서 
# conda install -c scitools cartopy
# 입력
# 마지막에
# Proceed ([y]/n)? 
# 질문이 나오면 'y'를 입력

# 카토피 참고 사이트
# https://scitools.org.uk/cartopy/docs/latest/crs/projections.html


import cartopy.feature as cfeature
import matplotlib.pyplot as plt

proj = ccrs.Mercator()
plt.figure(figsize=(10, 10))
# 최초의 창의 크기를 가로 세로 10인치로 설정

ax = plt.axes(projection = proj)
# projection <- 축 프로젝션의 형태

ax.set_extent((-25.0, 20.0, 52.0, 10.0))
# 주어진 좌표계에서 지도의 범위인 (좌, 우, 하, 상)을 설정

ax.add_feature(cfeature.LAND)
# 육지 추가

ax.add_feature(cfeature.OCEAN)
# 바다 추가

ax.add_feature(cfeature.COASTLINE)
# 해안선 추가

ax.add_feature(cfeature.BORDERS, linestyle=':')
# 육지의 지역별 경계 추가, linestyle에 ':'으로 입력하는 것은 파선으로 표현

plt.show()

# 처음 띄울 때에는 로딩시간이 걸림
'''
AI기초통계
12장 빅데이터의 가공
183페이지 중간-하단
20. 5. 18.
차재관 작성
'''

import pandas as pd
from numpy import NaN

robots = [
   [24, 23680],
   [35, NaN],
   [46, 47350],
   [27, NaN]
]

print(robots)
# 교안 183페이지의 중간과 하단의 내용은 넘파이 패키지에서 NaN모듈을 가져오지 않으면 에러가 난다는 의미임
'''
== 결과값 ==
[[24, 23680], [35, nan], [46, 47350], [27, nan]]
'''

# 184페이지 상단 계속 설명
data = pd.DataFrame(robots, columns=['max_speed', 'price']) # 판다스 데이터 프레임으로 저장
print(data) 

# 184페이지 중간 계속 설명
data.dropna(subset=['price'], axis=0, inplace=True)
data.dropna()
# price라는 곳에서 NaN가 있으면 행을 기준으로 전체 삭제
# inplace가 True이면 반환되는 것이 없음(자체가 수정되어 버림)

print(data) # NaN 포함된 행이 다 사라짐

data.dropna()
'''
==결과값==
   max_speed    price
0         24  23680.0
2         46  47350.0
'''

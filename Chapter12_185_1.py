
import pandas as pd
from numpy import NaN

robots = [
   [24, 23680],
   [35, NaN],
   [46, 47350],
   [27, NaN]
]

print(robots)
data = pd.DataFrame(robots, columns=['max_speed', 'price'])
mean = data['price'].mean() # price 항목의 평균을 연산
data.replace(NaN, mean) # 결측을 하기 위해 NaN을 mean으로 대체하겠다는 의도
print(data) # 이전에도 설명했지만 파이썬은 포인터 개념이므로 NaN이 그대로 살아있음

'''
==결과값==
   max_speed    price
0         24  23680.0
1         35      NaN
2         46  47350.0
3         27      NaN

'''

# 185페이지 하단을 계속 설명

data.replace(NaN, mean, inplace=True)

# 이전처럼 inplace 에 True를 설정해주면 반환되지 않아 데이터 자체가 수정됨
print(data) # Nan 값에 평균값으로 대체

'''
==결과값==
   max_speed    price
0         24  23680.0
1         35  35515.0
2         46  47350.0
3         27  35515.0
'''
# 통계적 의미를 갖추기 위해 missing value를 어떻게 처리해야 하느냐를 고민해야 함
# missing value 처리 방법은 1) 삭제하거나 2) 대치하는 방법이 있음

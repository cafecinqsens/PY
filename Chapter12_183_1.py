'''
AI기초통계
12장 빅데이터의 가공
183페이지 중간-하단
20. 5. 18.
차재관 작성
'''

import pandas as pd
import numpy as np
from numpy import NaN
# 넘파이 패키지에서 NaN 모듈을 가져와서 쓴다는 의미
# NaN은 Not a Number 라는 뜻으로 0 또는 빈칸을 의미


data = pd.DataFrame(np.arange(12).reshape(3, 4), columns=['A', 'B', 'C', 'D'])
# np(넘파이)를 통해 0부터 11까지 수를 추출하고 이를 reshape 메소드를 이용해 3행 4열의 행렬로 다시 구성
# 여기에 pd(판다스)의 데이터 프레임 메소드를 이용해 데이터를 담고 추가적으로 A, B, C, D의 열로 정리함

data.D[2] = 'NaN'
# data의 D열에 접근하여 2번 인덱스의 데이터에 NaN으로 저장
# 파이썬에서는 이를 포인터라는 개념을 사용함
# 통계적 의미를 갖기 위해서는 향후 결측이라는 개념(missing value)을 연결해서 생각해야 하기 때문에 NaN에 주목할 필요가 있음

print(data)

'''
==결과값==
   A  B   C    D
0  0  1   2    3
1  4  5   6    7
2  8  9  10  NaN
'''


# 183페이지 상단의 내용을 이어서 설명

print(data.drop(['D'], axis=1))
# drip 메소드는 데이터를 버리는(삭제하는) 것으로 위 처럼 특정 행이나 열을 기준으로 버릴 수 있다.
# 여기서 axis의 개념을 설명하면 '0'는 행(row, x축), '1'은 열(column, y축), '2'는 뎁스(depth, z축)를 기준으로 한다.
# 위의 인자값은 D열을 삭제하라는 의미이다.

'''
==결과값==
   A  B   C
0  0  1   2
1  4  5   6
2  8  9  10
'''
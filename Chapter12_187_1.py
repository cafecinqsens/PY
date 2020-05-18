'''
AI기초통계
12장 빅데이터의 가공
187페이지 중하단
20. 5. 18.
차재관 작성
'''

import numpy as np
import pandas as pd

# 교안에는 설명되어 있는 내용
# 생략되어 있지만 원 데이터를 생성 필요
raw_a = [
    [20, 100000],
    [30, 20000],
    [40, 500000],
]

a = pd.DataFrame(raw_a, columns=['age', 'income'])
a[:] = a[:].astype(float)
print(a)

'''
==결과값==
   age  income
0   20  100000
1   30   20000
2   40  500000
'''

# 187페이지 1번에 설명된 내용을 기준으로...0~1의 수 중 최대값 1을 목표로 연산함
a['age'] = a['age']/a['age'].max(axis=0)
a['income'] = a['income']/a['income'].max(axis=0) 


print(a)

'''
==결과값==
    age  income
0  0.50    0.20
1  0.75    0.04
2  1.00    1.00
'''

# 187페이지 2번에 설명된 내용을 기준으로...0~1의 수 중 최소값 0을 목표로 연산함
a['age'] = (a['age'] - a['age'].min(axis=0)) / (a['age'].max(axis=0) - a['age'].min(axis=0))
a['income'] = (a['income'] - a['income'].min(axis=0)) / (a['income'].max(axis=0) - a['income'].min(axis=0))

print(a)

'''
==결과값==
   age    income
0  0.0  0.166667
1  0.5  0.000000
2  1.0  1.000000
'''

# 188페이지 3번 설명된 내용을 기준으로

a['age'] = (a['age'] - a['age'].mean(axis=0)) / a['age'].std(axis=0)
a['income'] = (a['income'] - a['income'].mean(axis=0)) / a['income'].std(axis=0)

print(a)

'''
==결과값==
   age    income
0 -1.0 -0.414781
1  0.0 -0.725866
2  1.0  1.140647
'''


# 교안에서는 수학적으로 접근하여 정규화하였으나 파이썬에서는 간단한 코드로 지원하고 있음
# 정규화하는 코드
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler() 
a[:] = scaler.fit_transform(a[:])

print(a)

'''
==결과값==
   age    income
0  0.0  0.166667
1  0.5  0.000000
2  1.0  1.000000
'''

# 선형 회귀(Linear Regression)에서 위에서 처럼 2개의 속성 간 값 차이가 크면 안됨
# 따라서, 정규화(normalize)라는 과정이 필요
# 위의 코드를 쓰면 쉽게 정규화를 할 수 있으나 교재 저자의 의도는 정규화의 방법을 설명하기 위해 3가지 방법을 소개함


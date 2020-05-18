'''
AI기초통계
12장 빅데이터의 가공
190페이지 하단
20. 5. 18.
차재관 작성
'''

import numpy as np
import pandas as pd


ary = [
    [1, 1.1, '손'],
    [2, 2.2, '날개'],
    [3, 3.3, '손']
]

data = pd.DataFrame(ary, columns=['수온', '상온', 'hand'])

bi_x = pd.get_dummies(data['hand'])


# get_dummies()는 가변수를 만들어 주는 메소드
# 프로그램에서는 이항변수화(binarization)이라는 개념이 있음
# 이항변수화는 단순하게 '0'과 '1'의 개념으로 바꾸어 주는 것
# 간단히 설명하자면 데이터분석을 하기 위해서는 문자열을 0, 1의 조합으로 단순하게 해주는 것이 중요함
print(bi_x)

'''
==결과값==
   날개  손
0   0  1
1   1  0
2   0  1
'''

# 191페이지 연속

data1 = pd.concat([data, bi_x], axis=1, sort=False)
# 교안에서는 data라고 표현했지만 각 출력값을 구분하기 위해 data1로 표현
# concat 매소드는 2개의 데이터 프레임을 결합하는 것
# axis=1 열을 기준으로
# sort=False 정렬 안함

print(data1)

'''
==결과값==
   수온   상온 hand  날개  손
0   1  1.1    손   0  1
1   2  2.2   날개   1  0
2   3  3.3    손   0  1
'''

# 191페이지 하단 문제 계속
data1.drop(['hand'], axis=1, inplace=True)
# hand 컬럼을 열을 기준(axis=1)으로 반환해줄 것(inplace) 
# inplace를 안 쓸려면 data2 = data.drop(['hand'], axis=1)

print(data1)
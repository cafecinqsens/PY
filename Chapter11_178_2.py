'''
AI기초통계
11장 데이터 프레임 처리를 위한 Pandas
교안 178페이지 하단

20. 5. 18.
차재관 작성
'''

import pandas as pd


data = {
    'age': [23, 43, 12, 45],
    'name':['민준', '현우', '서연', '동현'],
    'height':[175.3, 180.3, 165.8, 172.7]
}

x = pd.DataFrame(data, columns=['name', 'age', 'height'])

index = [True, False, True, False]

print(x[index])
# 부울형 변수 index의 TRUE FALSE 값에 따라 행을 기준으로 출력 여부를 결정함
'''
==결과값==
  name  age  height
0   민준   23   175.3
2   서연   12   165.8
'''
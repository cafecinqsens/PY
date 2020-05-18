'''
AI기초통계
11장 데이터 프레임 처리를 위한 Pandas
교안 178페이지 중간

20. 5. 18.
차재관 작성
'''

import pandas as pd


data = {
    'age': [23, 43, 12, 45],
    'name':['민준', '현우', '서연', '동현'],
    'height':[175.3, 180.3, 165.8, 172.7]
}

x = pd.DataFrame(data)
# 사전형인 data 자체를 가지고 평균을 낼 수 없음
# 판다스의 데이터 프레임 형식으로 변환해줘야 함
print(x)
print(x.mean(axis=0))
# mean()은 평균을 내는 메소드
# axis=0은 행을 기준으로 연산
# 표준편차 -> std(), 분산 -> var(), 중앙값 -> median()
# 데이터 프레임 안에 텍스트가 있어도 연산하는데 문제 없음

'''
==결과값==
age        30.750
height    173.525
dtype: float64
'''
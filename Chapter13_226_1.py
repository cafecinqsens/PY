'''
AI기초통계
13장 빅데이터 분석 과제
교안 226페이지 상단

20. 5. 17.
차재관 작성
'''
import pandas as pd
import datetime as dt
import numpy as np
import matplotlib.pyplot as plt

birddata = pd.read_csv('bird_tracking.csv')
#csv형태의 파일 불러오기(저장 시 인코딩 방식을 UTF-8로 설정되었는지 확인)

ix = birddata.bird_name == 'Eric'
# Eric이라는 이름을 가진 새 데이터를 ix에 저장

speed = birddata.speed_2d[ix] 
# 컬럼 항목 중 'speed_2d'라는 것 중에 Eric 이름을 가진 것만 추출하여 'speed'에 저장

print(speed.head()) 
# 변수명.head()를 사용하면 상위 5개 행만 출력됨

'''
== 결과값 ==
0    0.150000
1    2.438360
2    0.596657
3    0.310161
4    0.193132
Name: speed_2d, dtype: float64
'''


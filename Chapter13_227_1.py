'''
AI기초통계
13장 빅데이터 분석 과제
교안 227페이지 중간

20. 5. 17.
차재관 작성
'''
import pandas as pd
import datetime as dt
import numpy as np
import matplotlib.pyplot as plt

birddata = pd.read_csv('/Users/bluewaves/Desktop/bird_tracking.csv')


speed = birddata.speed_2d[birddata.bird_name == 'Eric']
# Eric이라는 이름을 가진 speed_2d라는 데이터만 speed에 저장

print(speed[218])
# 218번 인덱스의 값을 출력

'''
결과값
0.786002544525143
'''

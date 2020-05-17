'''
AI기초통계
13장 빅데이터 분석 과제
교안 228페이지 상단

20. 5. 17.

차재관 작성
'''
import pandas as pd
import datetime as dt
import numpy as np
import matplotlib.pyplot as plt

birddata = pd.read_csv('/Users/bluewaves/Desktop/bird_tracking.csv')
speed = birddata.speed_2d[birddata.bird_name == 'Eric']


speed = np.array(speed)
# speed를 넘파이의 배열로 다시저장

print(np.isnan(speed))
# isnan을 사용해서 속도데이터가 nan이면 True를 그렇지 않으면 False로 반환함
'''
결과값
[False False False ... False False False]
'''

print(np.isnan(speed).any())
# nan이 하나라도 있으면 True로 표현함

'''
결과값
True
'''

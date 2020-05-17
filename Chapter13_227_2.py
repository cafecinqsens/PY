'''
AI기초통계
13장 빅데이터 분석 과제
교안 227페이지 하단

20. 5. 17.
차재관 작성
'''
import pandas as pd
import datetime as dt
import numpy as np
import matplotlib.pyplot as plt

birddata = pd.read_csv('/Users/bluewaves/Desktop/bird_tracking.csv')
speed = birddata.speed_2d[birddata.bird_name == 'Eric']
print(speed[219])
# 219번 인덱스의 값을 출력

'''
결과값
nan
'''

#nan은 not a number의 약자로 숫자가 아닌 데이터, 즉 데이터가 없다는 의미임


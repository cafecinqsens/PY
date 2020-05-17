'''
AI기초통계
13장 빅데이터 분석 과제
교안 226페이지 중간 -Quiz 13.24

20. 5. 17.
차재관 작성
'''
import pandas as pd
import datetime as dt
import numpy as np
import matplotlib.pyplot as plt

birddata = pd.read_csv('/Users/bluewaves/Desktop/bird_tracking.csv')
ix = birddata.bird_name == 'Eric'
# Eric 이라는 새의 이름을 가진 데이터를 ix에 저장
speed = birddata.speed_2d[ix]
# Eric의 speed_2d 데이터만 speed에 저장

plt.plot(range(50), speed[:50])
#왼쪽 인자값은 x축 데이터, 오른쪽 인자값은  y축 데이터

plt.xlabel('Observation')
plt.ylabel('Flying Speed')

plt.show()


# 교안 끝부분에 세미콜론(;)은 생략 가능하다. 
# 전통적인 프로그램에서는 세미콜론을 사용하여 한줄의 명령이 끝났음을 암시했다.
# 파이썬이나 스위프트(아이폰 앱 개발 프로그래밍 언어) 등 최신 프로그램들은 세미콜론을 생략해도 무방하다

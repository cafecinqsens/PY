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
print(np.isnan(speed))

def getnan(s):
    for i, n in enumerate(s):
        if np.isnan(n): # 인자값 n이 nan인지를 검증
            return i # nan이면 i로 반환

ind = getnan(speed)
# 사용자 함수 getnan을 실행하여 ind에 저장

print(ind)
'''
결과값
219
'''

print(len(np.isnan(speed)))
# speed에 nan이 얼마나 존재하는 지를 확인 <- 사실은 Eric에 대한 모든 데이터 개수임 Quiz 13.25에서 검증

'''
결과값
19795
'''

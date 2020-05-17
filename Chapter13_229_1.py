'''
AI기초통계
13장 빅데이터 분석 과제
교안 229페이지 하단

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
np.isnan(speed)

nanlist = []

def getnan(s):
    for i, n in enumerate(s):
        if np.isnan(n): # 인자값 n이 nan인지를 검증
            nanlist.append(i) # nan이면 i를 nanlist 추가함

getnan(speed)
# 사용자 함수 getnan을 실행
print('nan의 총개수:', len(nanlist))
# nanlist 개수 출력
print(nanlist)
# nanlist에 들어간 인덱스 번호를 출력

'''
== 결과값 ==
nan의 총개수: 85
[219, 1005, 1231, 1254, 1530, 1730, 2469, 3218, 3405, 3412, 3429, 3435, 3596, 3616, 3637, 3736, 3741, 4047, 4066, 4118, 4147, 4355, 4512, 4592, 4687, 4777, 4927, 4982, 5008, 5025, 5115, 5156, 5734, 5743, 5902, 6001, 6570, 6663, 6932, 6972, 7429, 7596, 8179, 8932, 9201, 9324, 9356, 9425, 9592, 10106, 10142, 10152, 10162, 10552, 10941, 10943, 11320, 12617, 12761, 13095, 13181, 13283, 14109, 14475, 14997, 15031, 15104, 15579, 15774, 15811, 15909, 16783, 16975, 17945, 18233, 18314, 19193, 19516, 19525, 19545, 19620, 19621, 19753, 19771, 19778]
'''


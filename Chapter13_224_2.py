'''
AI기초통계
13장 빅데이터 분석 과제
224페이지 상단
20. 6. 3.
차재관 작성
'''
import pandas as pd
import datetime as dt

birdata = pd.read_csv('bird_tracking.csv')
timestamps = []
# 빈 리스트 선언

for k in range(len(birdata)):
    timestamps.append(dt.datetime.strptime(birdata.date_time.iloc[k][:-3], '%Y-%m-%d %H:%M:%S'))
    # 인덱스 k행까지 -3 슬라이싱된 것을 timestamps에 추가해준다

birdata['timestamps'] = pd.Series(timestamps, index=birdata.index)
# birdata의 인덱스를 기준으로 timestamps를 추가해준다.


times = birdata.timestamps[birdata.bird_name == 'Eric']
# bird_name이 Eric인 것만 times에 저장한다.

elapsed = [time - times[0] for time in times]
# times에서 인덱스 값 0을 기준으로 빼준 것을 elapsed에 저장한다.

print(elapsed[100])
# 인덱스 100을 출력한다.

'''
= 결과값 =
1 days 05:24:41
'''

# 225페이지 상단
print(elapsed[0]) # 당연히 차이가 없다
print(elapsed[1])


'''
= 결과값 =
0 days 00:00:00
0 days 00:29:59
'''

# 225페이지 중간
print(elapsed[100]/dt.timedelta(days=1))
# timedealta에서 1일을 기준으로 수치화

'''
= 결과값 =
1.225474537037037
'''
# quiz 13.22
print(elapsed[100]/dt.timedelta(hours=1))
# 시간 기준은 hours

'''
= 결과값 =
29.41138888888889
'''

# 225페이지 하단
import matplotlib.pyplot as plt
import numpy as np

plt.plot(np.array(elapsed) / dt.timedelta(days=1))
# 넘파일 배열로 넣어서 1일 기준으로 수치화

plt.xlabel('Observation')
plt.ylabel('Elapsed(days)')
# x, y축 이름 


plt.show()


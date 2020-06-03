'''
AI기초통계
13장 빅데이터 분석 과제
223페이지 상단
20. 6. 3.
차재관 작성
'''
import pandas as pd
import datetime as dt

birdata = pd.read_csv('bird_tracking.csv')
date_str = birdata.date_time[0]

a = dt.datetime.strptime(date_str[:-3], '%Y-%m-%d %H:%M:%S')

print(a)
# 이전과 동일한 값이 출력

timestamps = []
# 빈 리스형 변수 timestamps 선언

for k in range(len(birdata)):
    timestamps.append(dt.datetime.strptime(birdata.date_time[k][:-3], '%Y-%m-%d %H:%M:%S'))
    # 오른쪽 3번째자리까지 슬라이싱된 k번째 행(birdata의 데이터 개수)까지 날짜 시간 형식에 맞추어 timestamps에 추가됨 

print(timestamps)

# 많은 데이터 값이 출력된다.

# 223페이지 중간
print(timestamps[1] - timestamps[0])
# 교안에서 잘못나왔다. birdata.timestamps가 아니다.
'''
=결과값=
0:29:59
'''

# 223페이지 하단
print(birdata.index)
'''
= 결과값 =
RangeIndex(start=0, stop=61920, step=1)
'''
# 1의 간격으로 인덱스 0에서 61920까지 있다는 의미

#223 페이지 하단

birdata['timestamps'] = pd.Series(timestamps, index = birdata.index)
# birdata의 인덱스를 기준으로 timestamps라는 1차원 배열을 저장

print(birdata.head())
# 앞 5개만 출력
'''
= 결과값 =
   altitude               date_time  device_info_serial   direction   latitude  longitude  speed_2d bird_name          timestamps
0        71  2013-08-15 00:18:08+00                 851 -150.469753  49.419859   2.120733  0.150000      Eric 2013-08-15 00:18:08
1        68  2013-08-15 00:48:07+00                 851 -136.151141  49.419880   2.120746  2.438360      Eric 2013-08-15 00:48:07
2        68  2013-08-15 01:17:58+00                 851  160.797477  49.420310   2.120885  0.596657      Eric 2013-08-15 01:17:58
3        73  2013-08-15 01:47:51+00                 851   32.769360  49.420359   2.120859  0.310161      Eric 2013-08-15 01:47:51
4        69  2013-08-15 02:17:42+00                 851   45.191230  49.420331   2.120887  0.193132      Eric 2013-08-15 02:17:42
'''


'''
AI기초통계
13장 빅데이터 분석 과제
220페이지 하단
20. 6. 3.
차재관 작성
'''
import pandas as pd
birdata = pd.read_csv('bird_tracking.csv')


print(birdata.columns)
# 열의 헤더 영역을 확인하는 것

'''
= 결과값 =
Index(['altitude', 'date_time', 'device_info_serial', 'direction', 'latitude',
       'longitude', 'speed_2d', 'bird_name'],
      dtype='object')
'''

# 221페이지 상단 코드 계속 
# 열의 헤더 영역 중 date_time 을 가져와서 인덱스 번호 0~2까지만 출력
print(birdata.date_time[0:3])

'''
= 결과값 =
0    2013-08-15 00:18:08+00
1    2013-08-15 00:48:07+00
2    2013-08-15 01:17:58+00
'''

# Quiz 13. 20 계속

ix = birdata.bird_name == 'Sanne'
date = birdata.date_time[ix]
print(date[:1])


'''
= 결과값 =
40916    2013-08-15 00:01:08+00
'''

# Quiz 13.21 계속

print(date[-1:])
'''
= 결과값 =
61919    2014-04-30 23:59:34+00
'''


'''
AI기초통계
13장 빅데이터 분석 과제
222페이지 중간
20. 6. 3.
차재관 작성
'''
import pandas as pd
import datetime as dt

birdata = pd.read_csv('bird_tracking.csv')
date_str = birdata.date_time[0]

print(date_str)

# 222페이지 중간 계속
print(date_str[:-3])
#슬라이싱 기법을 이용하여 끝에서 3자리 이전까지 표현

# 222페이지 하단 계속
print(dt.datetime.strptime(date_str[:-3], '%Y-%m-%d %H:%M:%S'))
# 형식에 맞추는 메서드 이지만 이미 형식을 갖추어서 큰 의미가 없다



'''
AI기초통계
13장 빅데이터 분석 과제
224페이지 상단
20. 6. 3.
차재관 작성
'''
import pandas as pd

birdata = pd.read_csv('bird_tracking.csv')

bird_names = pd.unique(birdata.bird_name)
# 유일한 원소를 찾아냄

print(bird_names)

'''
= 결과값 =
['Eric' 'Nico' 'Sanne']
'''


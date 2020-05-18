'''
AI기초통계
11장 데이터 프레임 처리를 위한 Pandas
교안 177페이지 중하단

20. 5. 18.
차재관 작성
'''

import pandas as pd

ary = [
    [1,2],
    [3,4],
    [5,6],
    [7,8],
    [9, 10],
    [11, 12]
]
# 참고를 위해 교안보다 하나 더 추가([11, 12])


data = pd.DataFrame(ary, columns=['First', 'Second'])


print(data.head())
# 데이터 프레임 처음 5개 줄만 출력

'''
==결과값==
   First  Second
0      1       2
1      3       4
2      5       6
3      7       8
4      9      10
'''

print(data.head(3))
# 데이터 프레임 처음 3개 줄만 출력

'''
==결과값==
   First  Second
0      1       2
1      3       4
2      5       6
'''


print(data.tail(3))
# 데이터 프레임 마지막 5개 줄만 출력

'''
==결과값==
   First  Second
2      5       6
3      7       8
4      9      10
'''

bools = [False, True, True, False, True, True]
# True 혹은 False값을 bools에 저장, 교안보다 인자값 True 하나 더 추가
print(data.Second[bools])
# data의 Second 열에 접근하여 bools의 False와 True를 기준으로 출력
'''
==결과값==
1     4
2     6
4    10
5    12
'''

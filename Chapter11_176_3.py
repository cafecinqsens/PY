'''
AI기초통계
11장 데이터 프레임 처리를 위한 Pandas
교안 176페이지 하단

20. 5. 18.
차재관 작성
'''

import pandas as pd

ary = [
    [1,2],
    [3,4],
    [5,6]
]

data = pd.DataFrame(ary, columns=['First', 'Second'])


print(data) # 전체 데이터 프레임을 출력
'''
==결과값==
   First  Second
0      1       2
1      3       4
2      5       6
'''

print(data.iloc[1]) # 1번 인덱스의 행 값을 출력

'''
==결과값==
First     3
Second    4
'''
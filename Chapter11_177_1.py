import pandas as pd

ary = [
    [1,2],
    [3,4],
    [5,6]
]

data = pd.DataFrame(ary, columns=['First', 'Second'])


print(data.iloc[:, -1])
# 앞쪽 인자값은 전체 행을 의미, 뒷쪽 인자값은 마지막 1개 값을 출력을 의미
'''
==결과값==
0    2
1    4
2    6
'''

print(data.iloc[:, 0])
# 뒷쪽 인자값을 0을 주면 첫번째 모든 행의 첫 번째데이터만 출력됨

'''
==결과값==
0    1
1    3
2    5
'''

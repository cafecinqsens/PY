'''
AI기초통계
11장 데이터 프레임 처리를 위한 Pandas
교안 179페이지 하단

20. 5. 18.
차재관 작성
'''

import pandas as pd
import numpy as np 

ary = [
  [1,2],
  [3,4],
  [5,6],
  [7,8],
  [9,10]
]

data = pd.DataFrame(ary, columns=['수온', '상온'])

data['수온'] = data['수온'].astype('float')

print(data)

'''
==결과값==
    수온  상온
0  1.0   2
1  3.0   4
2  5.0   6
3  7.0   8
4  9.0  10
'''



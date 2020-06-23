import pandas as pd
import numpy as np # 넘파이 패키지 추가

ary = [
  [1,2],
  [3,4],
  [5,6],
  [7,8],
  [9,10]
]

data = pd.DataFrame(ary, columns=['수온', '상온'])

print(data)


'''
==결과값==
   수온  상온
0   1   2
1   3   4
2   5   6
3   7   8
4   9  10
'''


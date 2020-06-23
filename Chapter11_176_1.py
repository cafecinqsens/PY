import pandas as pd

data = {
    'age': [23, 43, 12, 45],
    'name':['민준', '현우', '서연', '동현'],
    'height':[175.3, 180.3, 165.8, 172.7]
} 
#사전형에 대해서는 학습하지 않았는데 리스트형과 거의 비슷함
# 따옴표에 있는 스트링은 일반적으로 'key'라고 하고 콜론(:) 다음에 나오는 리스트형의 데이터를 'value' 라고 함

x = pd.DataFrame(data, columns=['name', 'age', 'height'])

print(x)


'''
==결과값==
   age name  height
0   23   민준   175.3
1   43   현우   180.3
2   12   서연   165.8
3   45   동현   172.7
'''

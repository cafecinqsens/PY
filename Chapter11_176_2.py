import pandas as pd

data = {
    'age': [23, 43, 12, 45],
    'name':['민준', '현우', '서연', '동현'],
    'height':[175.3, 180.3, 165.8, 172.7]
}
x = pd.DataFrame(data, columns=['name', 'age', 'height'])
print(x.name) # x다음에 점(.)을 찍고 해당 컬럼(colimn)명을 입력하면 해당 열만 출력


'''
==결과값==
0    민준
1    현우
2    서연
3    동현
'''

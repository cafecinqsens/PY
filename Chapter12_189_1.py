'''
AI기초통계
12장 빅데이터의 가공
189페이지 상단
20. 5. 18.
차재관 작성
'''

import numpy as np
import pandas as pd


price = np.random.randint(100, size=8)*10000
# 넘파이 패키지에서 랜덤 모듈을 가져와 랜덤으로 정수를 추출(randint)하는 메소드 사용
# 0 ~ 99 사이의 수 중 8개를 추출하여 10000을 곱해줌

cars = pd.DataFrame(price, columns=['price'])
# 판다스 데이터 프레임 형태로 price 데이터를 가져올 것이고 컬럼명을 price로 부여함

group_names = ['저급', '중급', '고급']
# 저급, 중급, 고급이라는 데이터를 가지고 있는 리스트형의 변수 선언


cars['Level'], mybin = pd.cut(cars['price'], 3, labels=group_names, retbins=True)
# 판다스에서 cut이라는 메소드는 binning하기 위한 도구임
# cars의 price에 저장되어 있는 데이터를 기준으로 3개 구간으로 그루핑
# 해당하는 구간명은 group_names의 데이터로 하고
# retbins(return bins)는 bin을 반환할 것인가를 묻는 것임
# 사실 mybin 변수는 생략해도 가능한데 반환되는 bin 값을 받기 위한 변수로 활용

print(cars)
'''
==결과값==
    price Level
0  740000    고급
1  560000    중급
2  460000    중급
3  150000    저급
4  980000    고급
5  920000    고급
6  450000    중급
7  630000    중급
'''

# 190페이지 상단 내용 계속
print(mybin)

'''
==결과값==
[149170.         426666.66666667 703333.33333333 980000.        ]
'''


'''
AI기초통계
12장 빅데이터의 가공
186페이지 중간
20. 5. 18.
차재관 작성
'''

import matplotlib.pyplot as plt
import numpy as np

x = np.random.randn(1000)
# 넘파이 패키지(np, numpy)에서 랜덤 모듈(random)을 이용하여 무작위 수 1,000개(randn)를 생성하여 x에 저장

plt.hist(x, density=True, bins=np.linspace(-5, 5, 21))

# plt.hist() -> 히스토그램으로 그리기
# density가 True면 확률로 False이면 빈도 수로 표현
# bins는 우리말로 표현하기는 어렵긴 하지만 구간 그룹이라고 할 수 있음
# 교안 186페이지 상단에 나와 있는 것처럼 연령 구간 그룹을 6개의 bin으로 구성할 수 있음
# 구간의 형태로 그루핑하는 것을 binning이라고 함
# linspace는 등간격이다. -5에서 5사이의 21개의 간격을 두고 싶다는 의미

plt.show()
# VSCODE 기준으로 실행 단축키는 (CTRL + F5, 맥버전에서도 동일함)
# 그래프가 생성되지 않으면 VSCODE 에디터 창 하단의 터미널 항목에서 우측에 있는 쓰레기통 아이콘을 클릭하여 클린한 상태에서 다시 실행

'''
AI기초통계
13장 빅데이터 분석 과제
207페이지 중간
20. 5. 21.
차재관 작성
'''
# csv 생성 필요
# github test.csv 참조
# 직접 생성 시 엑셀에서 빈칸 없이 아래와 같이 입력
'''
0 1 0
1 0 0
0 0 0
'''
# 엑셀 [다른이름 저장] -> [파일형식]: 쉼표로 구분된 값(.csv)
# 'could not convert string to float: '\ufeff0 ' 이런 오류 발생 시 엑셀 파일을 메모장으로 열어서 [다른 이름으로 저장]
# 저장창 맨 아래를 보면 인코딩 방식을 설정하는 드롭다운 메뉴 있음, ANSI -> UTF-8


import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

K = np.loadtxt('test.csv', delimiter=',')
# delimiter 는 쉼표로 구분한다는 의미
# 경로 오류가 나오면 test.csv 파일 절대 경로를 입력해 주어야 함
# 경로를 알아내는 방법은 해당 피일 선택 후 오른쪽 마우스 클릭, [속성] - [위치]에서 해당 절대 경로 복사
# 파이썬 피일과 csv 파일은 같은 폴더 내에 있어야 경로 오류가 나오지 않음

G = nx.to_networkx_graph(K)
# 다른 포맷으로부터 데이터를 가져와 그래프로 저장

nx.draw(G, with_labels=True, node_color='yellow', edge_color='red')

plt.show()
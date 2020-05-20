'''
AI기초통계
13장 빅데이터 분석 과제
202페이지 상단
20. 5. 20.
차재관 작성
'''

import networkx as nx
import matplotlib.pyplot as plt

G = nx.erdos_renyi_graph(25, 0.2) # 0.2의 확률로 25개 추출
nx.draw(G) # G에 저장된 그래프 생성

plt.show() # 출력되는 그래프는 매번 달라짐

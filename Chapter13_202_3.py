'''
AI기초통계
13장 빅데이터 분석 과제
202페이지 하단
20. 5. 20.
차재관 작성
'''

import networkx as nx
import matplotlib.pyplot as plt

G = nx.barabasi_albert_graph(25, 5) 
# barabasi_albert_graph(n, m) 바라바시 알버트 그래프
# n -> 노드의 개수
# m -> 새로운 노드로부터 존재하고 있는 노드까지 연결할 엣지의 개수

nx.draw(G) # G에 저장된 그래프 생성

plt.show() # 출력되는 그래프는 매번 달라짐


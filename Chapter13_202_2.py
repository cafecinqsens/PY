'''
AI기초통계
13장 빅데이터 분석 과제
202페이지 중간
20. 5. 20.
차재관 작성
'''

import networkx as nx
import matplotlib.pyplot as plt

G = nx.watts_strogatz_graph(30, 3, 0.1)
# nx.watts_strogatz_graph(n, k, p), 와츠 스트로가츠 그래프
# n -> 노드의 개수
# k -> 링 토폴로지(링 네트워크, 원형으로 모양을 구성)를 형성하며 각 노드는 가장 가까운 k 개의 이웃 노드에 연결
# p -> 각 엣지에 연결될 가능성

nx.draw(G) # G에 저장된 그래프 생성

plt.show() # 출력되는 그래프는 매번 달라짐

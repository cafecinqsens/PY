'''
AI기초통계
13장 빅데이터 분석 과제
210페이지 상단
20. 5. 25.
차재관 작성
'''
import networkx as nx
import matplotlib.pyplot as plt

G = nx.karate_club_graph() # 내장된 데이터를 가져와 G에 저장
nx.draw(G, with_labels=True, node_color='lightblue', edge_color='yellow')

print(G.degree()) #전체 연결 상태 확인

print(G.degree(16)) #특정 노드를 입력하면 연결된 차수를 확인 가능

print('노드의 개수: %d' % G.number_of_nodes()) # 노드의 개수 알아내기
print('엣지의 개수: %d' % G.number_of_edges()) # 엣지의 개수 알아내기

import numpy as  np

print('평균 차수: %.1f' % np.mean()) # 평균의 개수 알아내기



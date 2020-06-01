'''
AI기초통계
13장 빅데이터 분석 과제
211페이지 하단
20. 6. 1.
차재관 작성
'''
import networkx as nx
import matplotlib.pyplot as plt
import numpy as  np

G = nx.karate_club_graph() 

pos, degree = max([(n, d) for n, d in G.degree()])
# G에서 차수가 높은 노드를 출력하는 코드


print('노드: ', pos, ' 차수: ', degree)
# pos와 degree 값 출력

print(G.degree())

nx.draw(G, with_labels=True, node_size=100, node_color='yellow', edge_color='red')

plt.show()

# 노드 33번의 연결을 보면 연결되는 노드의 수가 가장 많은 것을 확인
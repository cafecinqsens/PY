'''
AI기초통계
13장 빅데이터 분석 과제
215페이지 하단
20. 6. 1.
차재관 작성
'''
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

K = np.loadtxt('social.csv', delimiter=',')
# 컴마(,)로 구분된 social.csv을 불러와 K에 저장
G = nx.to_networkx_graph(K)
# K를 networkx그래프로 저장

nx.draw(G, with_labels=True, node_color='yellow', edge_color='red')

plt.show()


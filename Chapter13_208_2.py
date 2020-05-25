'''
AI기초통계
13장 빅데이터 분석 과제
208페이지 하단
20. 5. 21.
차재관 작성
'''
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

K = np.loadtxt('test2.csv', delimiter=',')
G = nx.to_networkx_graph(K)
nx.draw(G, with_labels=True, node_color='yellow', edge_color='red')

plt.show() # 삼각형 형태의 그래프
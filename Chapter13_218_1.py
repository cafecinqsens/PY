'''
AI기초통계
13장 빅데이터 분석 과제
218페이지 상단
20. 6. 3.
차재관 작성
'''
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

K = np.loadtxt('social.csv', delimiter=',')

G = nx.to_networkx_graph(K)

def connected_component_subgraphs(G):
    for c in nx.connected_components(G):
        yield G.subgraph(c)

maxG = max(connected_component_subgraphs(G), key=len)

nx.draw(maxG, with_labels=True, node_color='yellow', edge_color='red')

plt.show()



'''
AI기초통계
13장 빅데이터 분석 과제
217페이지 상단
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

ksub = connected_component_subgraphs(G)


klist = list(ksub)

nx.draw(klist[0], with_labels=True, node_color='yellow', edge_color='red')
# 두개의 네트워크에서 0번 인덱스의 네트워크 그래프만 가져오는 코드

plt.show()


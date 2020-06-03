'''
AI기초통계
13장 빅데이터 분석 과제
218페이지 하단
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

minG = min(connected_component_subgraphs(G), key=len)
#교안과 다르게 구성, maxG -> minG

nx.draw(minG, with_labels=True, node_color='yellow', edge_color='red')
# 교안과 다르게 구성, maxG -> minG

plt.show()

#219~220페이지 두 개 Quiz 13.17, 13.18, 13.19 생략(social2.csv 파일 없음)




'''
AI기초통계
13장 빅데이터 분석 과제
204페이지 하단
20. 5. 21.
차재관 작성
'''



import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from scipy.stats import bernoulli

def erdosGraph(N, p):
    G = nx.Graph() 
    G.add_nodes_from(range(N))
    listG = list(G.nodes()) 
    for i, node1 in enumerate(listG):
        for node2 in listG[i+1:]: 
            if (bernoulli.rvs(p=p)): 
                G.add_edge(node1, node2) 
    return G

G1 = erdosGraph(80, 0.3)
plt.hist(list([d for n, d in G1.degree()]), histtype='step')
# list([d for n, d in G1.degree()]) -> 차수를 통해 노드와 엣지를 파악함
# histtype는 히스토그램의 타입으로 'bar', 'barstacked', 'step', 'stepfilled'이 있음

plt.show()

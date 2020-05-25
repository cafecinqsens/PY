'''
AI기초통계
13장 빅데이터 분석 과제
205페이지 중간
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

def pltGraph(G): # 커스텀 메서드를 통해 히스토그램을 생성함

    plt.hist(list([d for n, d in G.degree()]), histtype='step')

G1 = erdosGraph(80, 0.3) # 80번
pltGraph(G1)
G2 = erdosGraph(80, 0.3)
pltGraph(G2)
G3 = erdosGraph(80, 0.3)
pltGraph(G3)


plt.show() # 각기 다른 3개의 히스토그램 생성

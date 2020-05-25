'''
AI기초통계
13장 빅데이터 분석 과제
203페이지 하단
20. 5. 21.
차재관 작성
'''



import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from scipy.stats import bernoulli

def erdosGraph(N, p):
    G = nx.Graph() # 빈 그래프를 G에 저장
    G.add_nodes_from(range(N)) #0 ~  N-1 까지 노드 추가
    listG = list(G.nodes()) # 모든 노드를 리스트에 저장
    for i, node1 in enumerate(listG): # enumerate()는 인덱스 값을 포함하여 리턴함
        for node2 in listG[i+1:]: #이후에 노드 간 엣지로 연결하기 위해 인덱스 i에서 +1을 함
            if (bernoulli.rvs(p=p)): # p에는 0.18
                G.add_edge(node1, node2) # 자동으로 겹치지 않는 노드가 생성되어 복수의 엣지 추가
    return G

nx.draw(erdosGraph(20, 0.18)) 

plt.show()

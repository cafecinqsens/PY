'''
AI기초통계
13장 빅데이터 분석 과제
216페이지 중간
20. 6. 3.
차재관 작성
'''
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

K = np.loadtxt('social.csv', delimiter=',')


G = nx.to_networkx_graph(K)


# 교안에서 처럼 작성하면 에러가 나온다.
# connected_component_subgraphs()는 networkx 2.1버전에서 제거된 메서드이다.
# 교안의 의미를 최대한 살려서 한다면 다음과 같이 사용자 함수를 작성한다.
def connected_component_subgraphs(G):
    for c in nx.connected_components(G):
        yield G.subgraph(c)

ksub = connected_component_subgraphs(G)
# nx 패키지 사용하지 않고 사용자 함수를 활용한다.

klist = list(ksub)

print(len(klist))

'''
==결과값==
2
'''


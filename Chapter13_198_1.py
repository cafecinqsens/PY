'''
AI기초통계
13장 빅데이터 분석 과제
197페이지 상단
20. 5. 19.
차재관 작성
'''

import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
nx.add_path(G, [0,1,2,3])
# 교안에서는 G.add_path([0,1,2,3])은 안됨

print(G.degree(0)) # 노드 0에 엣지로 연결된 노드

'''
==결과값==
1
'''

print(G.degree([0, 1])) # 노드 0과 노드 1에 엣지로 연결된 노드들
'''
==결과값==
[(0, 1), (1, 2)]
'''
print(G.degree()) # 모든 노드의 연결 형태
'''
==결과값==
[(0, 1), (1, 2), (2, 2), (3, 1)]
'''


'''
AI기초통계
13장 빅데이터 분석 과제
198페이지 상단
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

# 198페이지 상단 설명 계속
print(G.edges())

'''
==결과값==
[(0, 1), (1, 2), (2, 3)]
'''

G.remove_edge(1, 2) # 노드 1과 2에 연결된 엣지 제거

print(G.edges())
'''
==결과값==
[(0, 1), (2, 3)]
'''

G.remove_edges_from([(1, 2), (1, 3)]) # 다수에 엣지를 제거할 때

print(G.edges())
# 교안에서는 아무것도 출력되지 않는다고 나오는데 답은 아래와 같음
# 이유는 (1,2)은 이미 위의 코드에서 엣지가 제거되었고, (1, 3)은연결되지 않은 상태임
'''
==결과값==
[(0, 1), (2, 3)]
'''

# (교안에는 없지만)만약 아무것도 출력되지 않는 결과값을 상정하고 제거한다면
G.remove_edges_from([(0, 1), (2, 3)]) 

print(G.edges())

'''
==결과값==
[]
'''
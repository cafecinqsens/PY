'''
AI기초통계
13장 빅데이터 분석 과제
196페이지 상단
20. 5. 19.
차재관 작성
'''

import networkx as nx
import matplotlib.pyplot as plt

# 이전 코드를 사용할 때에는 너무 길어지므로 교안과 달리 간단하게 처리함
G = nx.Graph()
raw_node = [1, 'P', 'Hi', 3, 4]
G.add_nodes_from(raw_node)
G.add_edge(1,2)

# 196페이지 설명 계속
G.add_edge(4,5)
print(G.edges())


'''
==결과값=
[(1, 2), (4, 5)]
정답 다): 노드 5가 없어서 노드 5를 새롭게 생성하고 4와 5을 연결하는 엣지 추가됨
'''

G.add_edges_from([(1,2), (1,3), (1,4), (1,5)])
print(G.edges())

'''
==결과값=
[(1, 2), (1, 3), (1, 4), (1, 5), (4, 5)]
중복되는 것은 빼고 없는 엣지만 추가적으로 생성됨
'''


# 196페이지 하단 
G.add_edges_from([(1, 'P'), (1, 'Hi')])
# 노드를 추가하는 코드를 작성하지 말고 바로 엣지를 연결하는 코드를 작성

nx.draw(G, with_labels=True, node_color='yellow', edge_color='red')
# 교안에서 제시한 라벨과 노드/엣지 색상 설정

plt.show()


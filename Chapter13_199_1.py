'''
AI기초통계
13장 빅데이터 분석 과제
199페이지 중간
20. 5. 20.
차재관 작성
'''

import networkx as nx

G = nx.Graph()
G.add_nodes_from([1,2,3,4,5])
G.add_edges_from([(1,2),(1,3),(1,4),(1,5),(4,5)])
#엣지와 노드를 추가

print('No. nodes:', G.number_of_nodes()) # 노드 갯수 출력
print('No. edges:', G.number_of_edges()) # 엣지 갯수 출력

'''
==결과값==
No. nodes: 5
No. edges: 5
'''

G.remove_edge(1,3) # 노드 1과 노드 3에 연결된 엣지 제거

print('No. nodes:', G.number_of_nodes()) # 노드 갯수 출력
print('No. edges:', G.number_of_edges()) # 엣지 갯수 출력
'''
==결과값==
No. nodes: 5
No. edges: 4
'''

# Quiz 13.5는 위와 같음

# 200페이지 설명 계속

G.remove_node(3) # 노드 3 제거

print('No. nodes:', G.number_of_nodes()) # 노드 갯수 출력
print('No. edges:', G.number_of_edges()) # 엣지 갯수 출력
'''
==결과값==
No. nodes: 4
No. edges: 4
'''

# 200페이지 Quiz 13.6
G.remove_node(4) # 노드 4 제거
print('No. nodes:', G.number_of_nodes()) # 노드 갯수 출력
print('No. edges:', G.number_of_edges()) # 엣지 갯수 출력

'''
==결과값==
No. nodes: 3
No. edges: 2
'''

# 201페이지 Quiz 13.7
G.remove_nodes_from([4, 5]) # 노드 4 제거
print('No. nodes:', G.number_of_nodes()) # 노드 갯수 출력
print('No. edges:', G.number_of_edges()) # 엣지 갯수 출력
'''
==결과값==
No. nodes: 2
No. edges: 1
'''
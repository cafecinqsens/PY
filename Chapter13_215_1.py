'''
AI기초통계
13장 빅데이터 분석 과제
215페이지 상단
20. 6. 1.
차재관 작성
'''
import networkx as nx
import matplotlib.pyplot as plt
import numpy as  np
import zipfile 

zf = zipfile.ZipFile('/Users/bluewaves/OneDrive/10.DEV/PY/football.zip')
txt = zf.read('football.txt').decode()
gml = zf.read('football.gml').decode()
gml = gml.split('\n')[1:]
G = nx.parse_gml(gml)

print('No. of nodes: %d' % G.number_of_nodes())
# 노드 수 출력
print('No. of edges: %d' % G.number_of_edges())
# 엣지 수 출력
print('Avg. of degrees: %.1f' % np.mean([d for n, d in G.degree()]))
# 평균 차수 출력

'''
== 결과값 == 
No. of nodes: 115
No. of edges: 613
Avg. of degrees: 10.7
'''
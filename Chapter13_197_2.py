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

nx.draw(G, with_labels=True, node_color='lightblue', edge_color='grey')
plt.show() # 0~3까지의 노드를 형성하고 엣지로 연결되는 구조


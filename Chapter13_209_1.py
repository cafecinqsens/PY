'''
AI기초통계
13장 빅데이터 분석 과제
209페이지 하단
20. 5. 25.
차재관 작성
'''
import networkx as nx
import matplotlib.pyplot as plt

G = nx.karate_club_graph() # 내장된 데이터를 가져와 G에 저장
nx.draw(G, with_labels=True, node_color='lightblue', edge_color='yellow')

plt.show()
'''
AI기초통계
13장 빅데이터 분석 과제
213페이지 상단
20. 6. 1.
차재관 작성
'''
import networkx as nx
import matplotlib.pyplot as plt
import numpy as  np

G = nx.karate_club_graph() 

degree = [d for n, d in G.degree()]
# 차수를 추출하여 저장

nx.draw(G, with_labels=True, node_size=[n*100 for n in degree], node_color='yellow', edge_color='red')
# 그래프를 G에 연결하고 라벨은 나오게, 노드 사이즈는 각 노드의 차수에 맞춰 사이즈 크기 다르게(크기를 통해 연결성 확인)
# 노드 컬러는 노란색, 엣지 컬러는 빨간색으로 표현

plt.show()
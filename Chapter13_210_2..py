'''
AI기초통계
13장 빅데이터 분석 과제
210페이지 하단
20. 6. 1.
차재관 작성
'''
import networkx as nx
import matplotlib.pyplot as plt
import numpy as  np

G = nx.karate_club_graph() 
plt.xlabel('Degree')
plt.ylabel('Prob. of node degree')

plt.hist(list([d for n, d in G.degree()]), histtype='step')

plt.show()
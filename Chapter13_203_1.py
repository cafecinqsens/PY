'''
AI기초통계
13장 빅데이터 분석 과제
203페이지 상단
20. 5. 20.
차재관 작성
'''

import networkx as nx
import matplotlib.pyplot as plt

G = nx.random_lobster(25, 0.9,0.9) 
# random_lobster(n, p1, p2)
# n -> (등뼈의) 예상되는 노드의 수
# p1 -> (등뼈의) 추가되는 엣지의 가능성
# p2 -> (등뼈에서) 벗어나는 한 개 수준의 추가되는 엣지의 가능성


nx.draw(G) # G에 저장된 그래프 생성

plt.show() # 출력되는 그래프는 매번 달라짐


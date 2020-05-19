'''
AI기초통계
13장 빅데이터 분석 과제
193페이지 상단
20. 5. 18.
차재관 작성
'''

import networkx as nx
G = nx.Graph()
# NetworkX 패키지의 그래프 모듈을 가져와 G에 저장


# 193페이지 중간 설명 계속
G.add_node(1) # 노드 1 추가
print(G.nodes())

'''
== 결과값 ==
[1]
'''
# 193페이지 중간 설명 계속
G.add_node('P') # 노드 P 추가
G.add_node('Hi') # 노드 Hi 추가
print(G.nodes())
'''
==결과값==
[1, 'P', 'Hi']
'''

# 193페이지 하단 설명 계속
G.add_nodes_from([2,3])  #노드 2, 3 추가
print(G.nodes()) 
'''
==결과값==
[1, 'P', 'Hi', 2, 3]
'''

# 194페이지 Quiz 13.1 설명 계속

for node in G: # 이제까지 추가된 노드는 G에 저장됨
   print(node)

'''
==결과값==
1
P
Hi
2
3
'''

# 194페이지 Quiz 13.2 설명 계속

G.add_nodes_from([3,4])
print(G.nodes())

'''
== 결과값 ==
[1, 'P', 'Hi', 2, 3, 4]

정답 나): 중복 요소는 제거되고 새로운 요소만 추가
'''


# 195페이지 상단 설명 계속

nx.draw(G, with_labels=True, node_color='lightblue')
# 네트워크 구조를 그리는 메서드 
# G는 연결할 노드
# with_labels 은 레이블 추가 여부
# node_color 는 노드에 색상 지정

import matplotlib.pyplot as plt
# 시각화를 위해 맷플롯립 패키지 가져오기

plt.show()
# 새로운 창이 나오지 않으면 VSCODE의 터미널 창을 Kill 하고 다시 실행
# 프로그램에서 실행을 런(Run)이라고 한다
# 단축키는 Ctrl+F5 또는 VSCODE 우측 상단 실행 버튼(재생 버튼)


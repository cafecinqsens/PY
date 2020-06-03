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
# 윈도우에서는 경로를 얻을 때에는 해당 파일(zip파일)을 선택하고 오른쪽 마우스 클릭
# 오른쪽 마우스 클릭 후 메뉴 리스트 중에 '속성'을 클릭, 창이 도출되면 가운데 부분에 '위치'라고 해서 경로를 복사할 수 있음
# 해당 경로를 ZipFile() 메서드에 적용함
# 그런데 그대로 작성하면 유니코드 에러 발생
# 파이썬은 역슬래시(\)를 유니코드로 인식함
# 따라서 역슬래시(\)를 일반 슬래시(/)로 변경하여 작성함
# zf = zipfile.ZipFile('C:/Users/owner/Desktop/football.zip')

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

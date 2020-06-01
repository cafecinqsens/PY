'''
AI기초통계
13장 빅데이터 분석 과제
214페이지 하단
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

print(G.degree())
# G.degree() 로 출력
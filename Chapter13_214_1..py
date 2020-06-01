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
import zipfile # 파이썬에서 집파일 압축 및 해제하기 기능



zf = zipfile.ZipFile('/Users/bluewaves/OneDrive/10.DEV/PY/football.zip')
txt = zf.read('football.txt').decode()
gml = zf.read('football.gml').decode()
# gml(geographical markup language)은 지리정보 파일을 의미

gml = gml.split('\n')[1:]
# 스플릿 -> 떼어놓다\, '\n' -> 한줄씩 

G = nx.parse_gml(gml)
# gml 파일을 파싱(사용자 의도에 따라 추출하는 것)하여 G에 저장

nx.draw(G, with_labels=True)
# 교안에는 없지만 추가해 준다

plt.show()
# 교안에서는 savefig()을 사용했지만 굳이 그럴 필요가 없음
# 그래프 창이 뜨면 좌측 하단 아이콘 중에 디스크 모양을 클릭하여 직접 저장 가능


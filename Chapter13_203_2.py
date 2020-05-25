'''
AI기초통계
13장 빅데이터 분석 과제
203페이지 중간
20. 5. 21.
차재관 작성
'''

import networkx as nx
from scipy.stats import bernoulli
# Scipy는 파이썬 기반 패키지(라이브러리)
# 다양한 통계관련 도구를 제공하는데 단순 수치적 접근뿐 아니라 공학적 개념까지 해결할 수 있음

# 본 내용을 수행하기 위해 베르누이 시행 모듈을 임포트함
# 결과가 두 가지 중 하나로만 나오는 실험이나 시행을 베르누이 시행(Bernouilli Trial)
# 동전을 던져 앞면(Head, H)이 나오거나 뒷면(Tail, T)가 나오게 하는 것이 베르누이 시행


for i in range(6):
    print(bernoulli.rvs(p=0.33))
    # 베르누이 확률변수(Bernouilli Random Variable) -> 베르누이 시행 결과를 0과 1로 바꾼 것을 말함
    # p는 확률

'''
==결과값===
0
0
1
1
1
0
'''
# 결과값은 매번 달라진다
# 33%의 확률로 1이 나오게 하는 것임 대력 6번 중에 2번 정도가 나오는 것이 일반적임
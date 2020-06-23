import pandas as pd
import numpy as np 

accident = pd.read_csv('acci.csv', engine='python')
# csv 파일을 쉼표로 구분된 형식으로 저장하여 불러들임
# 한글로 저장하고 싶으면 원파일에서 '쉼표로 구분된 UTF-8 csv 확장자'로 저장 

print(accident)


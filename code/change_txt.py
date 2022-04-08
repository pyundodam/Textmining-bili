import pandas as pd
from encodings import utf_8
import re

df = pd.read_excel("C:/Users/adoba/Desktop/2022_업무/Git-hub Project/Textmining-bili/file/bili_Keyword_IU.xlsx") #변환할 엑셀파일 열기
df_drop_null = df.dropna(axis=0) # 엑셀에서 열이 없는 행을 제거

title_list = df_drop_null[0].values.tolist() # 엑셀에서 열이 없는 행을 제거한 데이터 중 Title을 리스트로 변환

with open('value_test.txt(2)','w',encoding='UTF-8') as f: #출력할 txt 파일 이름 설정
    for title in title_list:
        f.write(title+'\n')

f.close()

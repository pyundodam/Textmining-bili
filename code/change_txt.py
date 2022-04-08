from cProfile import label
from operator import index
from this import d
import pandas as pd
from encodings import utf_8
import re

df = pd.read_excel("C:/Users/adoba/Desktop/2022_업무/Git-hub Project/Textmining-bili/file/bili_Keyword_IU.xlsx")
df_drop_null = df.dropna(axis=0) # 엑셀에서 열이 없는 행을 제거
# df_drop_firstrow = df_drop_null.drop([0]) # 첫번째 행을 제거

# df_drop_null[0].drop(columns=0)

# value_list = df_drop_firstrow[0].values.tolist() #데이터 프레임 제목 값만 리스트로 변형
value_list = df_drop_null[0].values.tolist()

# line = list(df_drop_null[0])
# line_txt = pd.DataFrame(line)

# line_txt.to_csv("full_txt3.txt",sep = "\t", index = False, encoding = "utf-8") # 엑셀에서 열이 없는 행을 제거

# open = open("full_txt3.txt", "r")
# lines = open.readlines()
# lines[1:] 

# print(lines)

# write = open("value_test.txt", "w")
# f = write.strip(lines[0])

with open('value_test.txt(2)','w',encoding='UTF-8') as f:
    for title in value_list:
        f.write(title+'\n')

f.close()

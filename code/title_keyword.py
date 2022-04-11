from encodings import utf_8
from openpyxl import Workbook
import stanza
from collections import Counter
import pandas as pd
import re

stanza.download('zh',processors='tokenize,pos')
nlp = stanza.Pipeline('zh', processors='tokenize,pos')

read_txt = open("bili_Keyword_舞蹈_full.txt","r",encoding="utf-8").readlines()

def regex_txt(text): # 전처리 함수
    parse = re.sub(r'[^\w\s]','',text)
    num = re.sub(r'\d+',' ',parse)
    eng = re.sub('[a-zA-Z]' , ' ', num)
    null = eng.replace('\n',' ')
    return null

def get_words(text): # 형태소 분석 함수
    text = nlp(text)
    txt = [f'{text.text}' for text in text.sentences for text in text.words]
    return txt

data = [] # 리스트에 형태소를 넣음
n=0

for i in read_txt:
    pos = regex_txt(read_txt[n])
    data.append(get_words(pos))
    n+=1

# print(data) # 형태소가 리스트에 저장됨 #0번방이 colum3의 0번 행과 결합하면 됨

#기존 엑셀에 형태소 분석 결과 삽입

excel = pd.read_excel('bili_Keyword_舞蹈.xlsx') #기존 column3을 가져옴 (데이터프레임 형태)

column = excel.drop(['Unnamed: 0'],axis=1)
column2 = column.drop([1],axis=1)
column3 = column2.drop(['Unnamed: 3'],axis=1) #엑셀에서 필요없는 열 제외하고 column3만 남겼음

# print(column3)

column3['word'] = data
column3.to_excel('bili_Keyword_舞蹈_Keyword.xlsx')
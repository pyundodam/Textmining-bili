from encodings import utf_8
from openpyxl import Workbook, load_workbook
import openpyxl
import stanza
from collections import Counter
import pandas as pd
import re
import os

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


for i in read_txt:
    pos = regex_txt(str(read_txt))

count = get_words(pos)
# print(count)

data_count = Counter(count)
# remove_counter = Counter({x : count[x] for x in count if len (x) < 1})
# HF_keyword = remove_counter.most_common()
HF_keyword = data_count.most_common()

export_count = pd.DataFrame(HF_keyword)

with pd.ExcelWriter("완성본.xlsx",mode="a",engine="openpyxl") as writer :
    export_count.to_excel(writer, sheet_name = "Count", index = False)





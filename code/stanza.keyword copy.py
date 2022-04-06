from encodings import utf_8
from pickletools import read_stringnl_noescape
import stanza
from collections import Counter
import pandas as pd
import re

excel = pd.read_excel('bili_Keyword_舞蹈.xlsx')

column = excel.drop(['Unnamed: 0'],axis=1)
column2 = column.drop([1],axis=1)
column3 = column2.drop(['Unnamed: 3'],axis=1)

# print(column3) #데이터 프레임 형태로 출력되는 것 확인

def text_cleaning(column3):
    parse = re.sub(r'[^\w\s]','',column3)
    num = re.sub(r'\d+',' ',parse)
    eng = re.sub('[a-zA-Z]' , ' ', num)
    null = eng.replace('\n',' ')
    return null

column3[0]=column3[0].apply(lambda x: text_cleaning(x))
# column3.to_excel('column3_test.xlsx') #엑셀 출력 문제 없는 것 확인

# print(column3)



# def get_words(text):
#     stanza.download('zh',processors='tokenize,pos')
#     nlp = stanza.Pipeline('zh', processors='tokenize,pos')
#     text = nlp(column3[0].astype(str))
#     # txt = [f'{text.text}' for text in text.sentences for text in text.words]
#     pos = [f'{text.text}' for text in text.sentences for text in text.words]
#     # txt = [f'{text.text}' for text in text.words]
#     return pos

# # for i in column3[0]:
# #     c = column3[0]

# df = get_words(column3)
# print(df)

# column3["words"]=column3[0].apply(lambda x: get_words(x))

# d = column3["words"]
# print(d)

# column3.to_excel('column3_test(2).xlsx')

# print(get_words(column3)) #형태소 분석 가능한 것 확인



# print(column3)


# def get_words(text):
#     list = [list.text for list in text.sentences]
#     txt = [f'{text.text}' for text in text.sentences for text in text.words]
#     return txt

# print(txt)


# df = pd.DataFrame({"text":txt},index=range(0,len(txt)))
# print(df)

# column3['txt']=column3[0].apply(lambda x: text_cleaning(x))
# print(column3)

# # print(null)

# a = pd.DataFrame(column3,columns=['text'])
# print(a)
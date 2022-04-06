from encodings import utf_8
import stanza
from collections import Counter
import pandas as pd
import re

stanza.download('zh',processors='tokenize,pos')
nlp = stanza.Pipeline('zh', processors='tokenize,pos')
read = open("bili_Keyword_舞蹈_full.txt","r",encoding="utf-8").read()
text = nlp(read) #분석할 내용 입력

# parse = re.sub(r'[^\w\s]','',read)
num = re.sub(r'\d+',' ',read)
eng = re.sub('[a-zA-Z]' , ' ', num)
null = eng.replace('\n',' ')
# org = ' '.join(null.split())


df = pd.DataFrame(null.split())
# print(df)

df.to_excel('test(2).xlsx')
# for i in text:
#     list = [list.text for list in nlp.sentences]
#     print(list)
#     txt = [f'{text.text}' for text in text.sentences for text in text.words]
#     pos = [f'{text.xpos}' for text in text.sentences for text in text.words]

# # print(frame)
# df = pd.DataFrame({"text":txt,"pos":pos},index=range(0,len(txt)))

# print(df)
# # df.to_excel('stanza_test.xlsx') #출력한 데이터 엑셀에 저장
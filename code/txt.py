from encodings import utf_8
import stanza
from collections import Counter
import pandas as pd
import re

stanza.download('zh',processors='tokenize,pos')
nlp = stanza.Pipeline('zh', processors='tokenize,pos')

read = open("bili_Keyword_舞蹈_full.txt","r",encoding="utf-8").read()
text = nlp(read) #분석할 내용 입력

parse = re.sub(r'[^\w\s]','',read)
num = re.sub(r'\d+',' ',parse)
eng = re.sub('[a-zA-Z]' , ' ', num)
null = eng.replace('\n',' ')

df = pd.DataFrame({"text":null},index=[0]) #값이 가로로 나옴 (22.04.06)
print(df)

# def get_words(text):
#     text = nlp(null)
#     txt = [f'{text.text}' for text in text.sentences for text in text.words]
#     return txt


# print(get_words(df[0]))

# df["word"]=df.apply(lambda x: get_words(x))
# print(df)
# df.to_excel("word.xlsx")
from encodings import utf_8
import stanza
from collections import Counter
import pandas as pd
import re

stanza.download('zh',processors='tokenize,pos')
nlp = stanza.Pipeline('zh', processors='tokenize,pos')

read_txt = open("bili_Keyword_舞蹈_full.txt","r",encoding="utf-8").readlines()

def regex_txt(text):
    parse = re.sub(r'[^\w\s]','',text)
    num = re.sub(r'\d+',' ',parse)
    eng = re.sub('[a-zA-Z]' , ' ', num)
    null = eng.replace('\n',' ')
    return null

def get_words(text):
    text = nlp(text)
    txt = [f'{text.text}' for text in text.sentences for text in text.words]
    return txt

def pos_data(list):
    for i in range(len(list)):
        df = get_words(regex_txt(list[i]))
        return df



# print(get_words(df[0]))

# df["word"]=df.apply(lambda x: get_words(x))
# print(df)

# df2.to_excel("test(2).xlsx")
from encodings import utf_8
import stanza
from collections import Counter
import pandas as pd

stanza.download('zh',processors='tokenize,pos')
nlp = stanza.Pipeline('zh', processors='tokenize,pos')
text = nlp("我爱北京天安门")

list = [list.text for list in text.sentences]
txt = [f'{text.text}' for text in text.sentences for text in text.words]
pos = [f'{text.xpos}' for text in text.sentences for text in text.words]

# print(frame)
df = pd.DataFrame({"text":txt,"pos":pos},index=range(0,len(txt)))

# print(df)
df.to_excel('stanza_test.xlsx')
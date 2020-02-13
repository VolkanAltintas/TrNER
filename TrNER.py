import polyglot
from polyglot.text import Text
from collections import Counter

dataSet='insert here your txt file path....'
with open(dataSet,encoding='utf-8') as f: 
    data = f.readlines() 

dataStr=listToString(data)
doc = Text(dataStr)
for sent in doc.sentences:
  for entity in sent.entities:
    print(entity.tag, entity)

labels = [x.tag for x in doc.entities]
Counter(labels)

items=[]
for x in doc.entities:
  items=items+ x
Counter(items).most_common(10)
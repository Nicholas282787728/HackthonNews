import json
import nltk
import numpy as np
from nltk.corpus import stopwords
#nltk.download()
outfile=open("data","w")
#stories: id, score, time, kids, descendants, title, url, text
#comment: id, time, parent
#1959807
#stops = set(stopwords.words('the'))
#id, time, descendants
def data(dct):
    if 'dead' in dct and dct['dead']==True:
        return 0
    if 'descendants' not in dct:
        dct['descendants']=0
    if 'id' in dct and 'score' in dct and 'time_ts' in dct and 'title' in dct and 'url' in dct:
        if 'descendants' not in dct:
            dct['descendants']='0'
        if 'text' not in dct:
            dct['text']=" "
        if 'title' not in dct:
            dct['title']=" "
        
        return (dct['id'], str(dct['title'].lower()), str(dct['text'].lower()), str(dct['time_ts']), str(dct['score']), str(dct['descendants']))
    return 0

Xdata=[]
f=open('./stories','r')
i=0
while i<1959807:
    line=f.readline()
    json.dumps(line, sort_keys=True,indent=4, separators=(',', ': '))
    result=json.loads(line,object_hook=data)
    if result!=0:
        outfile.write(str(result))
        outfile.write('\n')
    i+=1

Xdata=np.asarray(Xdata)
f.close()
outfile.close()




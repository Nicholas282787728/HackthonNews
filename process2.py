import json
import nltk
import numpy as np
import enchant
import random
import string
from nltk.corpus import stopwords
stop=['the', 'is', '\'s', 'am', 'are', 'was', 'were', 'be', 'a', 'an', '<', '>', '/', ';', ':', ',', '.', '?', '[', ']', '{', '}', '$', '&', '^', '&', '*', '(', ')', '\'\'', '\`\`', '-', '#', '|', '',]
#nltk.download()
outfile=open("train.dat","w")
index_file=open("table4", "w")
#stories: id, score, time, kids, descendants, title, url, text
#comment: id, time, parent
#1959807
#filtered_words = [word for word in word_list if word not in stopwords.words('the')]
def data(dct):
    if 'dead' in dct or 'time_ts' not in dct:
        return 0
    if 'kids' not in dct:
        dct['kids']=[]
    if 'descendants' not in dct:
        dct['descendants']=0
    if 'id' in dct and 'time_ts' in dct and 'title' in dct and 'score' in dct and 'url' in dct:
        if 'text' not in dct or dct['text']=="":
            dct['text']=" "
        if 'title' not in dct:
            dct['title']=" "
        return (dct['id'], str(dct['title'].lower()), str(dct['text'].lower()), str(dct['time_ts']), str(dct['url']), str(dct['score']), str(dct['descendants']), dct['kids'])
    return 0

def break_sen(sentence):
    
    delset = string.punctuation
    sentence = sentence.translate(delset)
    tokens=nltk.word_tokenize(sentence)
    tokens=[str(word) for word in tokens if str(word) not in stop]
    tagged = nltk.pos_tag(tokens)
    result=''
    for word in tagged:
        if word[1] in ['NNP', 'NNPS', 'NN', 'NNS']:
            result+=word[0]
            result+=' '
    return result

def merge(t1,t2):
    list=[]
    for word in t1:
        if word not in list:
            list.append(word)
    for word in t2:
        if word not in list:
            list.append(word)
    return list

def make_sen(result):
    tokens=break_sen(result)
    sen=''
    for word in tokens:
        sen+=word
        sen+=' '
    print (sen)
    return sen

f=open('./stories','r')
i=1700
while i<1959807:
    line=f.readline()
    rand=random.randint(1, 49)
    if rand%7 >0:
        #print (rand)
        i+=1
        continue
    json.dumps(line, sort_keys=True,indent=4, separators=(',', ': '))
    result=json.loads(line,object_hook=data)
    if result!=0:
        sentence=break_sen(result[1])
        outfile.write(str(sentence))
        outfile.write('\n')
        index_file.write(result[0])
        index_file.write('\t')
        index_file.write(result[1])
        index_file.write('\t')
        index_file.write(result[2])
        index_file.write('\t')
        index_file.write(result[3])
        index_file.write('\t')
        index_file.write(result[4])
        index_file.write('\t')
        index_file.write(result[5])
        index_file.write('\t')
        index_file.write(result[6])
        index_file.write('\t')
        index_file.write(str(result[7]))
        index_file.write('\n')
    i+=1
    if i%10000==1:
        print (i)
f.close()
outfile.close()
index_file.close()









import pandas as pd
import numpy as np
import json
import os
from datetime import datetime

def compute(Count,Sum):
    return pd.DataFrame({'time':Sum['time']})


#    ,'count/story': Sum['descendent']/Count['id']

cell=[]
f=open('story_class0.data','r')
i=0
while i<2000:
    line=f.readline()
    result = json.dumps(line, sort_keys=True,indent=4, separators=(',', ': '))

    # Insert tuple into list
    cell.append(result)
    i+=1

# Convert list into Dataframe for data processing
df = pd.DataFrame(cell)

# Change here according to ur input
df = pd.DataFrame(df[0].str.split(',',5).tolist(),columns = ['id','title','text','time','kids','descendent'])
print df

def convert(df):
# Change her to drop columns you dont want, comment out if necessary
    df = df.drop(['text','title','kids'],1)
#print df

    # This is to remove unnecessary strings
    df['id'] = df['id'].str[4:-1]
    df['time'] = df['time'].str[2:12]
    #df['score'] = df['score'].str[2:4]
    df['descendent'] = df['descendent'].str[2:-4]


    df.time = df.time[~df.time.str.contains('[a-zA-Z]|\'| \[ | \]')]
    df.descendent = df.descendent[~df.descendent.str.contains('[a-zA-Z]')]
    df.descendent = df.descendent.str.replace('\'','')

    #print df.descendent

    df =df.dropna()
    df.index= range(0,np.size(df.time))

    # To convert dataframe into timestamp
    for i in range(0,np.size(df.time)):
    #print df.time[i]
        df.time[i] = datetime.strptime(df.time[i],'%Y-%m-%d')
        df.descendent[i] = int(df.descendent[i])


        Sort = df.sort_index(by='time')
        Sort.index = range(0,np.size(Sort.time))

        return Sort

#group by intervals of time, count # item, sum of descendent
grouper = Sort.groupby(pd.TimeGrouper(freq='W',key='time'))
print '***** grouper'
#print grouper


#final = pd.DataFrame( columns = ['comment', 'score'])

#num = grouper.count() % grouper.sum()

final = grouper.count()
final2 = grouper.sum()

#print final
print '                 *****'
print final2
#in terms of dataframe
List = compute(final,final2)
print List

#final.index = range(0,np.size(final.id))
#print num

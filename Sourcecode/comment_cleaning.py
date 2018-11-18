import pandas as pd
import numpy as np
import json
import os

#df = pd.DataFrame(data)
array=[]
outfile=open("comment_clean","w")

def data(dct):
    if 'deleted' in dct and dct['deleted']==True:
        return 0

    return (dct['id'], dct['time_ts'], dct['parent'])

f=open('comments_000000000000','r')
i=0
while i<262703:
    line=f.readline()
    json.dumps(line, sort_keys=True,indent=4, separators=(',',':'))
    result=json.loads(line,object_hook=data)
    if result!=0:
        array.append(result)
        outfile.write(str(result))
        outfile.write('\n')
    i += 1
#array=np.asarray(array)
#df = pd.DataFrame(array, columns=['id', 'time', 'parent', 'ranking'])
#aggregrate(df)


#df is a series
#df = df[0].str.replace(' " ', ' ')
#df = df.str.strip()

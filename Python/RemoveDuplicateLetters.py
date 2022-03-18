from collections import Counter
from time import sleep
from typing import List
def remove(s:str)->str:
    res=[]
    lastIndex={}
    for i in range(len(s)):
        lastIndex[s[i]]=i
    lastIndex=dict(sorted(lastIndex.items(), key=lambda x:x[1]))

    start=0
    for key in lastIndex.keys():
        temp='z'
        while(key not in res):
            for i in s[start:lastIndex[key]+1]:
                if i<temp and i not in res:
                    temp=i
                    start=start + s[start:lastIndex[key]+1].index(i)+1
            res.append(temp)
            temp='z'
    return ''.join(res)
        

remove("cbacdcbc")
remove("bcabc")
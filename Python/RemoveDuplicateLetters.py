from collections import Counter
from typing import List
def remove(s:str)->str:
    res=[]
    lastIndex={}
    for i in range(len(s)):
        lastIndex[s[i]]=i
    lastIndex=dict(sorted(lastIndex.items(), key=lambda x:x[1]))

    start=0
    for index in lastIndex.values():
        temp='z'
        
        for i in s[start:index+1]:
            if i<temp and i not in res:
                temp=i
                start=s.index(i)
        res.append(temp)
    print(res)
        

remove("cbacdcbc")
remove("bcabc")
from itertools import count
from time import sleep
from typing import List, OrderedDict
from collections import Counter
def partitionLabels(s:str)->List[int]:
    res=[]
    lastIndex={}
    for i in range(len(s)):lastIndex[s[i]]=i

    curr=0
    i=0
    while curr<len(s):
        tail=list(lastIndex.keys())[i]
        tempPartition=s[curr:lastIndex[tail]+1]
        countItems=Counter(tempPartition)
        def isValidPartition():
            for j in countItems:
                if lastIndex[j]>lastIndex[tail]: return j
            return True
        
        isValid=isValidPartition()
        if isValid==True:
            res.append(len(tempPartition))
            curr=lastIndex[tail]+1
            try:
                i=list(lastIndex.keys()).index(s[curr])
            except: break

        else:
            i=list(lastIndex.keys()).index(isValid)

    return res

print(partitionLabels("eccbbbbdec"))
print(partitionLabels("aebbedaddc"))
print(partitionLabels("ababcbacadefegdehijhklij"))
print(partitionLabels("aaaaaaaaaaa"))
print(partitionLabels("bababcbacadefegdehijhklij"))
print(partitionLabels("a"))
print(partitionLabels("bababcbacadefegdehijhklijbababcbacadefegdehijhklijbababcbacadefegdehijhklijbababcbacadefegdehijhklijbababcbacadefegdehijhklijbababcbacadefegdehijhklijbababcbacadefegdehijhklijbababcbacadefegdehijhklijbababcbacadefegdehijhklijbababcbacadefegdehijhklijbababcbacadefegdehijhklijbababcbacadefegdehijhklijbababcbacadefegdehijhklijbababcbacadefegdehijhklijbababcbacadefegdehijhklijbababcbacadefegdehijhklijbababcbacadefegdehijhklijbababcbacadefe"))
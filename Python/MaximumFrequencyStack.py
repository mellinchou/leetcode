import collections
from typing import Collection


class FreqStack:
    def __init__(self):
        self.freq = Collection.Counter()
        self.m = collections.defaultdict(list)
        self.maxf = 0

    def push(self, x):
        freq, m = self.freq, self.m
        freq[x] += 1
        self.maxf = max(self.maxf, freq[x])
        m[freq[x]].append(x)

    def pop(self):
        freq, m, maxf = self.freq, self.m, self.maxf
        x = m[maxf].pop()
        if not m[maxf]: self.maxf = maxf - 1
        freq[x] -= 1
        return x

    # def __init__(self):
    #     self.stack=[]
    #     self.mydict={}
    #     self.maxfreq={0:0}

    # def push(self, val: int) -> None:
    #     self.stack.append(val)
        
    #     if val in self.mydict: self.mydict[val]+=1
    #     else: self.mydict[val]=1
            
        

    # def pop(self) -> int:
    #     listOfKeys=list()
    #     for key, value in self.mydict.items():
    #         if value==max(self.mydict.items(), key=lambda x: x[1])[1]:
    #             listOfKeys.append(key)
    #     tail=len(self.stack)-1
    #     for i in range(tail, -1, -1):
    #         if self.stack[i] in listOfKeys:
    #             maxValue=self.stack[i]
    #             del self.stack[i]
    #             self.mydict[maxValue]-=1
    #             return maxValue
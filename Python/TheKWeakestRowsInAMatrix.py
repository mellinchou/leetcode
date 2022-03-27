from typing import List
from collections import Counter
def kWeakestRows(mat: List[List[int]], k: int) -> List[int]:
    numSoldiers=[]
    for i in range(len(mat)):
        count=0
        for j in range(len(mat[i])):
            if mat[i][j]==1: count+=1
            else: break
        numSoldiers.append([i, count])
    numSoldiers=sorted(numSoldiers, key=lambda x:x[1])
    res=[]
    for i in range(k):
        res.append(numSoldiers[i][0])
    print(res)

kWeakestRows([[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]], 3)
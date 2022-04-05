from collections import Counter
from typing import List
def minDominoRotations(tops: List[int], bottoms: List[int]) -> int:
    topCount, botCount=Counter(tops),Counter(bottoms)
    same=Counter()
    for a,b in zip(tops,bottoms):
        if a==b:
            same[a]+=1
    for i in range(1,7):
        if topCount[i]+botCount[i]-same[i] == len(tops):
            return min(topCount[i], botCount[i])-same[i]
    return -1
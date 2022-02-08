from typing import List
from collections import Counter

def topKFrequent(words: List[str], k: int) -> List[str]:
    counter = Counter(words)
    maxK = []
    for i in range(0, k):
        maxKeys=[key for key, value in counter.items() if value == max(counter.values())]
        maxKey=sorted(maxKeys)[0]
        maxK.append(maxKey)
        counter.pop(maxKey)
    print (maxK)

topKFrequent(["i","love","leetcode","i","love","coding"],3)

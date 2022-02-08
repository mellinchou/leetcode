from typing import List
from collections import Counter


def topKFrequent(nums: List[int], k: int) -> List[int]:
    counter = Counter(nums)
    maxK = []
    for i in range(0, k):
        maxKey = max(counter, key=counter.get)
        maxK.append(maxKey)
        counter.pop(maxKey)
    return maxK

topKFrequent([1,1,1,2,2,3],2)

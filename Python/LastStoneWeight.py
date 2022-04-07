from typing import List
def lastStone(stones: List[int])->int:
    
    while len(stones)>1:
        stones.sort()
        x, y =stones[len(stones)-1], stones[len(stones)-2]
        stones=stones[:len(stones)-2]
        if x-y>0:
            stones.append(x-y)
    if len(stones)==1: return stones[0]
    else: return 0

print(lastStone([1]))
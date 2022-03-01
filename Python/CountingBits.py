from typing import List
def countBits(n: int) -> List[int]:
    res=[0]
    carry=0
    while len(res)<n+1:
        index=0
        for i in range (2**carry, min(2**(carry+1), n+1)):
            res.append(res[index]+1)
            index+=1
        carry+=1
    return res
    # for i in range(2**carry, 2**(carry+1)):
    #     print (i)

print(countBits(5))
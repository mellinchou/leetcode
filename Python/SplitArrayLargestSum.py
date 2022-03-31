from typing import List
def split(nums: List[int], m:int) -> int:
    l, r = 0,0
    for i in nums:
        l = max(l, i)
        r += i
    while l < r:
        mid = l + (r-l)//2
        
        tempSum=0
        tempPieces=1
        for i in nums:
            if tempSum+i > mid:
                tempSum=i
                tempPieces+=1
            else: 
                tempSum+=i
        
        if tempPieces > m:
            l=mid+1
        else: 
            r=mid
    return l

print(split([7,2,5,10,8],2))
            
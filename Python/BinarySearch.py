import math
from typing import List
def search(nums: List[int], target: int) -> int:
    l, r = 0, len(nums)-1
    mid=int((l+r)/2)
    while l<=r:
        if nums[mid]==target: return mid
        elif nums[mid]<target: 
            l = mid+1
        elif nums[mid]>target: 
            r = mid-1
        mid=int((l+r)/2)
    return -1


print(search([0,1,2],0.5))
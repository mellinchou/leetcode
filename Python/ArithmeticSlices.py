from typing import List
def numberOfArithmeticSlices(nums: List[int]) -> int:
    if len(nums)<3: return 0
    curr = sum = 0
    for i in range (2, len(nums)):
        if nums[i]-nums[i-1]==nums[i-1]-nums[i-2]:
            curr+=1
            sum+=curr
        else: curr=0
    return sum

    # def isArithmetic(slice: List[int]) -> bool:
    #     diff=slice[1]-slice[0]
    #     for i in range(0, len(slice)-1):
    #         if slice[i+1]-slice[i]!=diff: return False
    #     return True
    
    # if len(nums)<3: return 0
    # count=0
    # for i in range(0,len(nums)-1):
    #     for j in range(i+3, len(nums)+1):
    #         if isArithmetic(nums[i:j]):count+=1
    # return count

print(numberOfArithmeticSlices([1,2,3,4]))
print(numberOfArithmeticSlices([1,2]))
print(numberOfArithmeticSlices([1,2,3,5]))
print(numberOfArithmeticSlices([1,2,5,6,7,8]))
print(numberOfArithmeticSlices([]))

from typing import List
import collections
def threeSum(nums: List[int]) -> List[List[int]]:
    res=[]
    nums.sort()
    repeatedCount=0
    if (len(nums)>0):curr=nums[0]
    compliments={}
    for i in range (0, len(nums)):
        if nums[i]==curr: repeatedCount+=1
        else: repeatedCount=1
        if repeatedCount>3: continue

        threeSumCompliment = 0 - nums[i]
        for j in range (i+1, len(nums)):
            if nums[j] in compliments.keys() and len(compliments[nums[j]])==2:
                compliments[nums[j]].append(nums[j])
                if compliments[nums[j]] not in [elem for elem in res]: res.append(compliments[nums[j]]) 
            twoSumCompliment = threeSumCompliment - nums[j]
            compliments[twoSumCompliment]=[nums[i],nums[j]]
        compliments.clear()
    print(res)

threeSum([])
threeSum([1,-1,0])
threeSum([1,2,-2,-1])
threeSum([-1,0,1,2,-1,-4])
threeSum([0,8,2,-9,-14,5,2,-5,-5,-9,-1,3,1,-8,0,-3,-12,2,11,9,13,-14,2,-15,4,10,9,7,14,-8,-2,-1,-15,-15,-2,8,-3,7,-12,8,6,2,-12,-8,1,-4,-3,5,13,-7,-1,11,-13,8,4,6,3,-2,-2,3,-2,3,9,-10,-4,-8,14,8,7,9,1,-2,-3,5,5,5,8,9,-5,6,-12,1,-5,12,-6,14,3,5,-11,8,-7,2,-12,9,8,-1,9,-1,-7,1,-7,1,14,-3,13,-4,-12,6,-9,-10,-10,-14,7,0,13,8,-9,1,-2,-5,-14])

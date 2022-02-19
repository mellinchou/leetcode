from typing import List
def threeSum(nums: List[int], target: int) -> List[int]:
    myDict = {}
    for i in range (0, len(nums)):
        compliment = target - nums[i]
        if (compliment in myDict.keys()):
            return [i, myDict[compliment]]
        myDict[nums[i]]=i
    print(myDict)

print(threeSum([2,7,11,15], 9))
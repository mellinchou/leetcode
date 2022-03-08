from typing import List
def removeElement(self, nums: List[int], val: int) -> int:
    if len(nums)==0: return 0
    k=len(nums)
    for i in range(len(nums)):
        while nums[i]==val and k>i:
            k-=1
            nums.append(nums[i])
            nums.remove(nums[i])
    return k
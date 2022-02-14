# Problem: Finding the intersection of 2 arrays, res[] shouldn't have repeated elements
# Solution: Convert both arrays to sets, iterate over the smaller set to check if element exist in bigger set

from typing import List
def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
    set1=set(nums1)
    set2=set(nums2)
    res=[]

    if(len(set1)>len(set2)):
        for i in set2:
            if i in set1 and i not in res:
                res.append(i)
    else:
        for i in set1:
            if i in set2 and i not in res:
                res.append(i)
    print(res)
    

# Naive Solution: 2 for-loops

# def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
#     res=[]
#     for i in nums1:
#         for j in nums2:
#             if (i==j and i not in res):
#                 res.append(i)
#     print(res)



intersection([1,2,2,1], [2,2])
intersection([4,9,5], [9,4,9,8,4])
intersection([], [2,2])
intersection([1], [2])

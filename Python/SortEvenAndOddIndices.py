from typing import List

def sortEvenOdd(nums: List[int]) -> List[int]:
    odd=[]
    even=[]
    res=[]
    for i in range (0,len(nums)):
        if (i%2 ==0):
            even.append(nums[i])
        else:
            odd.append(nums[i])
    
    even.sort(reverse=False)
    odd.sort(reverse=True)

    for i in range (0,len(nums)):
        if (i%2 ==0):
            res.append(even.pop(0))
        else:
            res.append(odd.pop(0))
            
    print(res)


sortEvenOdd([4,1,2,3])
sortEvenOdd([2,1])
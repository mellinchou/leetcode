from typing import List
def plusOne(digits: List[int]) -> List[int]:
    carry=False
    digits[len(digits)-1]+=1
    for i in range(len(digits)-1,-1,-1):
        if carry==True:
            digits[i]+=1
            carry=False
        if digits[i] == 10:
            digits[i]=0
            carry=True
    if carry==True: digits.insert(0,1)
    return digits
        

print(plusOne([1,2,3]))
print(plusOne([9,9,9]))
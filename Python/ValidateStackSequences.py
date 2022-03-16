from typing import List
def validateStackSequences(pushed: List[int], popped: List[int]) -> bool:
    curr=popped[0]
    i=0
    while i<len(pushed) and len(pushed)>0:
        if pushed[i]==curr:
            pushed.remove(pushed[i])
            popped.remove(curr)
            if popped:curr=popped[0]
            i=max(0, i-1)
            print(pushed, popped)
        else: i+=1
    
    if pushed or popped: return False
    else: return True

print(validateStackSequences([0,2,1],[0,1,2]))
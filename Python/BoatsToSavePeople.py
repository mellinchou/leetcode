from typing import List
def numRescueBoats(people: List[int], limit: int) -> int:
    res=0
    people=sorted(people)
    head=0
    tail=len(people)-1
    while head<=tail:
        if head==tail:
            res+=1
            break
        elif people[tail]==limit: 
            res+=1
            tail-=1
        elif people[head]+people[tail]<=limit:
            res+=1
            head, tail = head+1, tail-1
        else:
            res+=1
            tail-=1
    return res

print(numRescueBoats([3,2,2,1], 3))
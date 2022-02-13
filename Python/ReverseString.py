from typing import List
import math
def reverseString(s: List[str]) -> None:
    tail=len(s)-1
    for i in range (0, math.ceil(len(s)/2)):
        temp=s[i]
        s[i]=s[tail]
        s[tail]=temp
        tail-=1
    return s

print(reverseString(["h","e","l","l","o"]))
print(reverseString(["H","a","n","n","a","h"]))
print(reverseString(["H"]))
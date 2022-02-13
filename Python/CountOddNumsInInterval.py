import math

def countOdds(low: int, high: int) -> int:
    count=math.floor((high-low)/2)
    if (low%2==1 or high%2==1):count+=1
    print(count)

countOdds(9,9)
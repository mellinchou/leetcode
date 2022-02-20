def countEven(num: int) -> int:
    count=0
    
    for i in range(1, num+1):
        sum=0
        for j in str(i):
            sum+=int(j)
        if sum%2==0: count+=1
    return count
print(countEven(4))
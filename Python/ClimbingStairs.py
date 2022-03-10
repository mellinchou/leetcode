def climbStairs(n: int) -> int:
    # recursive fibonacci takes too long
    # if n==1: return 1
    # if n==2: return 2
    # return climbStairs(n-1)+climbStairs(n-2)
    
    # a more mathematical way to obtain the fibonacci number
    a, b = 1, 1
    for i in range(n):
        a, b = b , a+b
    return a

print(climbStairs(38))
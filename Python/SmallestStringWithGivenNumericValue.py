def getSmallestString(n: int, k: int) -> str:
    res=['a']*n
    alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    
    score = n # current score with all set to 'a'
    tail=n-1
    while score!=k:
        print(f"res={res}, tail={tail}, score={score}")
        if k-score>=26:
            res[tail] = 'z'
            score+=25
        else:
            res[tail]= alphabet[int((k-score)%26)]
            score = score + int((k-score)%26)
        tail-=1
    
    return ''.join(res)

print(getSmallestString(5,73))
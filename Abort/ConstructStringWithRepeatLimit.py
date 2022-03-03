def repeatLimitedString(s: str, repeatLimit: int) -> str:
    sortedS=''.join(sorted(s, reverse=True))
    res='d'
    count=0
    curr=sortedS[0]
    i=0
    while len(sortedS)!=0 and i<len(sortedS):
        if(sortedS[i]==curr):
            count+=1
            i+=1
        else:
            count=1
            curr=sortedS[i]
            i+=1
        
        if count>repeatLimit:
            res+=sortedS[:i-1]
            sortedS=sortedS[i-1:]
            for char in sortedS:
                if char != curr:
                    res+=char
                    curr=char
                    count=0
                    sortedS=sortedS.replace(char, '', 1)
                    i=0
    if len(sortedS)!=0:
        if res[len(res)-1] != sortedS[0]:
            res+=sortedS
    res=res.replace('d', '' , 1)
    
    print(res)

repeatLimitedString("cczazcc",3)
repeatLimitedString("aababab",2)
repeatLimitedString("a",1)
repeatLimitedString("aababab",1)
repeatLimitedString("aabababaaaaaaaaooooooooooooooooooooooooaaaaaifjjjjjjjjjjj",2)
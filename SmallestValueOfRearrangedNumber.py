def smallestNumber(num: int) -> int:
    splited=[a for a in str(num)]
    count=0

    if(splited[0]=='-'):
        splited.pop(0)
        splited.sort(reverse=True)
        splited.insert(0,'-')
    else:
        splited.sort(reverse=False)
        while(len(splited)>1 and splited[0]=='0'):
            splited.pop(0)
            count+=1
        for i in range(0,count): 
            splited.insert(1,'0')
    
    res="".join(splited)
    res=int(res)
    print(res)

smallestNumber(0)
smallestNumber(-50100)
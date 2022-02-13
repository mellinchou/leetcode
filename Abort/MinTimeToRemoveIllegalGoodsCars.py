def minimumTime(s: str) -> int:
    count=0
    indices=[]

    for i in range (0, len(s)):
        if (s[i]=='1'):
            indices.append(i)
    
    print(indices)
    head=False
    tail=False
    temp=0

    for i in range (0,len(indices)):
        if (indices[i]==0): 
            count+=1
            head=True
        elif (head==True and indices[i]-indices[i-1]==1): 
            count+=1
        elif (tail==True and indices[i]-indices[i-1]==1):
            temp+=1
        elif (tail==False):
            head=False
            temp+=1
            tail=True
        else:
            count+=temp*2
            tail=False
            temp=1
    
    if (indices[-1]!=len(s)-1): count+=temp*2
    else: count+=temp

    
    print(count)


minimumTime("010110")


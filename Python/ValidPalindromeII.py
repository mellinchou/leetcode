def validPalindrome(s: str) -> bool:
    def isPalindrome(s):
        head=0
        tail=len(s)-1
        while(head<tail):
            if s[head]!=s[tail]: 
                return False
            else:
                head+=1
                tail-=1
        return True
    
    head=0
    tail=len(s)-1
    while(head<tail):
        if s[head]!=s[tail]: 
            tempA=s[:head]+s[head+1:]
            tempB=s[:tail]+s[tail+1:]
            return isPalindrome(tempA) or isPalindrome(tempB)
        else:
            head+=1
            tail-=1
    return True


print(validPalindrome("abbbb"))

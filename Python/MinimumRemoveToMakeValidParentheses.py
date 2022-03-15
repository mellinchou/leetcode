def minToRemove(s: str) -> str:
    stack=[]
    s = list(s)
    for char in range(len(s)):
        if s[char]=='(':
            stack.append(char)
        elif s[char]==')':
            if stack: stack.pop()
            else: 
                s[char]=''
    while stack:
        s[stack.pop()]=''
    return ''.join(s)

print(minToRemove("lee(t(c)o)de)"))
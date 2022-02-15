from pickle import FALSE


def isValid(s: str) -> bool:
    myDict={ "(":")", "[":"]", "{":"}"}
    myStack=[]
    if (len(s)%2!=0): return False

    for char in range(0, len(s)):
        if s[char] in myDict.keys():
            myStack.append(myDict[s[char]])
        elif (len(myStack)==0):
            return False
        elif myStack[len(myStack)-1] == s[char]:
            myStack.pop(len(myStack)-1)
        else: return False
    if (len(myStack)==0): return True
    else: return False

print(isValid("()[]"))
print(isValid("("))
print(isValid("(]()]"))
print(isValid(""))
print(isValid("([])()"))
print(isValid("([]))"))
print(isValid("([][])"))
print(isValid(")["))
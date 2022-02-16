from curses.ascii import isdigit
import math

def myAtoi(s:str) -> int:
    isPositive=True
    isLeadingSpace=True
    hasSign=False
    myInteger="0"
    for char in s:
        if (isLeadingSpace==True and char==' '): continue
        elif (isLeadingSpace==False and char==' '): break
        elif (char=='-' and myInteger=="0" and hasSign==False): 
            isLeadingSpace=False
            isPositive=False
            hasSign=True
        elif (char=='+' and myInteger=="0" and hasSign==False): 
            isLeadingSpace=False
            hasSign=True
        elif (char.isdigit()):
            isLeadingSpace=False
            myInteger+=char
        else: break

    if (myInteger==''): return (0)

    myInteger=int(myInteger)
    if isPositive==False:
        myInteger=int(myInteger)*-1
    
    if (myInteger>2147483648):myInteger=2147483648
    elif (myInteger<-2147483648):myInteger=-2147483648
    print(myInteger)

myAtoi("  -42")
myAtoi("42 425")
myAtoi("4193 with words")
myAtoi("words and 987")
myAtoi("00-3")
myAtoi("22s")
myAtoi("s11")
myAtoi("3.14")
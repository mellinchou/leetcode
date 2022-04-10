from typing import List
def calPoints(ops: List[str]) -> int:
    points=[]
    for i in range(len(ops)):
        if ops[i]=="+":
            points.append(points[-1]+points[-2])
        elif ops[i]=='C':
            points=points[:-1]
        elif ops[i]=='D':
            points.append(points[-1]*2)
        else:
            points.append(int(ops[i]))
    res=0
    for i in points:
        res+=i
    return res
    

print(calPoints(["5","-2","4","C","D","9","+","+"]))
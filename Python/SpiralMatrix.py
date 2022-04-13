from typing import List
def generateMatrix(n:int)->List[List[int]]:
    res=[[0]*n for i in range(n)]
    currRow=0
    currCol=0
    currDir=1 # 1 for right, 2 for down, 3 for left, 4 for up
    currRowBorder=n
    currColBorder=n
    currRowBegin=1
    currColBegin=0
    for i in range(n*n):
        res[currRow][currCol]=i+1
        if currDir==1:
            if currCol+1<currColBorder:
                currCol+=1
            else:
                currDir=2
                currColBorder-=1
                currRow+=1
        elif currDir==2:
            if currRow+1<currRowBorder:
                currRow+=1
            else:
                currDir=3
                currRowBorder-=1
                currCol-=1
        elif currDir==3:
            if currCol-1>=currColBegin:
                currCol-=1
            else:
                currDir=4
                currColBegin+=1
                currRow-=1
        elif currDir==4:
            if currRow-1>=currRowBegin:
                currRow-=1
            else:
                currDir=1
                currRowBegin+=1
                currCol+=1
    print(res)

generateMatrix(4)
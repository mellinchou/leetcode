from typing import List
def rotate(matrix: List[List[int]]) -> None:
    for i in range(0, len(matrix)):
        for j in range (i, len(matrix[i])):
            if i==j: continue
            matrix[i][j], matrix[j][i]=matrix[j][i], matrix[i][j]
    for row in range(0, len(matrix)):
        i=0
        j=len(matrix[row])-1
        while i<j:
            matrix[row][i], matrix[row][j]=matrix[row][j], matrix[row][i]
            i+=1
            j-=1
    print(matrix)

    # 00 01 02
    # 10 11 12
    # 20 21 22
    
rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]])
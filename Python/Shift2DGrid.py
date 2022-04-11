from typing import List
def shiftGrid(grid: List[List[int]], k: int) -> List[List[int]]:
    res=[[0] * len(grid[i]) for i in range(len(grid))]
    for i in range(len(grid)):
        for j in range (len(grid[i])):
            shiftRow=(((k+j)//len(grid[i]))+i)%len(grid)
            shiftCol=(k+j)%len(grid[i])
            res[shiftRow][shiftCol]=grid[i][j]
    return res

print(shiftGrid([[1,2,3,4],[4,5,6,6],[7,8,9,9]],1))
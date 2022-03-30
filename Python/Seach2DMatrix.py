from typing import List
def search(matrix: List[List[int]], target: int) -> bool:
    topRow, botRow = 0, len(matrix)-1
    searchRow=-1
    while topRow<=botRow:
        midRow = (topRow+botRow)//2
        if matrix[midRow][0]<=target<=matrix[midRow][-1]:
            searchRow=midRow
            break
        elif target<matrix[midRow][0]:
            botRow=midRow-1
        elif target>matrix[midRow][-1]:
            topRow=midRow+1
    if searchRow==-1: 
        return False
    
    l, r = 0, len(matrix[searchRow])-1
    while l<=r:
        mid=(l+r)//2
        if matrix[searchRow][mid]==target: return True
        elif target<matrix[searchRow][mid]: r=mid-1
        elif target>matrix[searchRow][mid]: l=mid+1
    
    return False

print(search([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 66))
from typing import List
def gameOfLife(board: List[List[int]])->None:
    def countNeighbors(i,j)->int:
        count=0
        for k in range(i-1, i+2):
            for l in range(j-1, j+2):
                if k<0 or k>=len(board) or l<0 or l>=len(board[0]): continue
                if k==i and l==j: continue
                if board[k][l]==1: count+=1
        return count
    
    neighbors=[]
    for i in range(len(board)):
        for j in range(len(board[i])):
            neighbors.append(countNeighbors(i,j))
    
    index=0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if neighbors[index]<2: board[i][j]=0
            elif board[i][j]==0 and neighbors[index]==3: board[i][j]=1
            elif neighbors[index]>3: board[i][j]=0
            elif board[i][j]==1 and 2<=neighbors[index]<=3: board[i][j]==1
            index+=1
    print(board)

gameOfLife([[0,1,0],[0,0,1],[1,1,1],[0,0,0]])

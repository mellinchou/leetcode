def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        tower=[[0.0 for i in range (query_glass+2)] for j in range (query_row+1)]
        tower[0][0]=poured
        
        for i in range(0, query_row):
            for j in range(0, query_glass+1):
                overflow=max(0, tower[i][j]-1.0)
                tower[i+1][j]+=overflow/2.0
                tower[i+1][j+1]+=overflow/2.0
        return min(1.0, tower[query_row][query_glass])
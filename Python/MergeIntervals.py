from typing import List
def merge(intervals: List[List[int]]) -> List[List[int]]:
    intervals=sorted(intervals, key=lambda x: (x[0]))
    i=0
    while i<len(intervals)-1:
        if (intervals[i][1]>intervals[i+1][0]):
            intervals[i][1]=max(intervals[i][1], intervals[i+1][1])
            del intervals[i+1]
        else: i+=1
    return intervals

# merge([[1,3],[2,6],[8,10],[15,18]])
# merge([[1,4],[4,5]])
# merge([[1,1],[1,2]])
# merge([[1,1]])
# merge([[1,4],[0,4]])
merge([[0,2],[1,9],[2,5],[10,11],[0,2],[12,20],[19,20],[0,3],[1,1]])
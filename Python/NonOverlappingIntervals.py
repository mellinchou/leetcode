from typing import List
def eraseOverlapIntervals(intervals: List[List[int]]) -> int:
    intervals=sorted(intervals, key=lambda x: x[0])
    count=0
    i=0
    while i<len(intervals)-1:
        if intervals[i][1]>intervals[i+1][0]:
            if intervals[i][1] > intervals[i+1][1]: del intervals[i]
            else: del intervals[i+1]
            count+=1
        else: i+=1
    return count

print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))
print(eraseOverlapIntervals([[1,100],[11,22],[1,11],[2,12]]))
print(eraseOverlapIntervals([[1,2],[1,2],[1,2]]))
print(eraseOverlapIntervals([[1,2],[2,3]]))
print(eraseOverlapIntervals([[1,2]]))
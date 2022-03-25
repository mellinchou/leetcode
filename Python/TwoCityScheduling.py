from typing import List
def schedule(cost: List[List[int]])->int:
    extraCost=[]
    for i in range (len(cost)): extraCost.append([i,cost[i][1]-cost[i][0]])
    extraCost=sorted(extraCost, key=lambda x:x[1])
    
    totalCost=0
    for i in range(len(extraCost)):
        if i<int(len(cost)/2):
            totalCost+=cost[extraCost[i][0]][1]
        else:
            totalCost+=cost[extraCost[i][0]][0]
    return totalCost

print(schedule( [[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]]))
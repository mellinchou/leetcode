from typing import List

def permute(nums: List[int]) -> List[List[int]]:
    res=[]
    dfs([],nums,res)
    return res

def dfs(pivot, options, res):
    if not options: 
        res.append(pivot)
        return
    for char in range(0, len(options)):
        dfs(pivot + [options[char]], options[:char] + options[char+1:], res)

print(permute([1,2,3]))
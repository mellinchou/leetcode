from typing import List
def longestCommonPrefix(self, strs: List[str]) -> str:
    pivot=min(strs, key=len)
    for i in range (0, len(strs)):
        for j in range (0, len(pivot)):
            if (strs[i][j]==pivot[j]): 
                continue
            else:
                pivot=pivot[:j]
                break
    return pivot



longestCommonPrefix(["reflower","flow","flight"])
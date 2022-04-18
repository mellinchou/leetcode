from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        nums=[]
        def dfs(node):
            if node==None: return
            nums.append(dfs(node.left))
            nums.append(node.val)
            nums.append(dfs(node.right))
            return
        
        count=0
        dfs(root)
        for i in nums:
            if i!=None:
                count+=1
                if count==k: return i
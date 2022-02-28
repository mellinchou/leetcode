# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, leftVal, rightVal):
            if not root: return True
            if root.val<=leftVal or root.val>=rightVal: return False
            else: return dfs(root.left, leftVal, root.val) and dfs(root.right, root.val, rightVal)
        
        return dfs(root, float('-inf'), float('inf'))
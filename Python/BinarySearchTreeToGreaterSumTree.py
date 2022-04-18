# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def treeSum(node):
            if node==None: return 0
            return node.val+treeSum(node.left)+treeSum(node.right)
        
        def dfs(node, prev):
            if node==None: return
            node.val=node.val+treeSum(node.right)+prev
            node.right=dfs(node.right,prev)
            node.left=dfs(node.left, node.val)
            return node
        
        return dfs(root,0)
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class BSTIterator:
    
    def __init__(self, root: Optional[TreeNode]):
        self.nums=[]
        self.curr=0
        def dfs(node):
            if node==None: return
            dfs(node.left)
            self.nums.append(node.val)
            dfs(node.right)
        dfs(root)

    def next(self) -> int:
        res=self.nums[self.curr]
        self.curr+=1
        return res

    def hasNext(self) -> bool:
        if self.curr>=len(self.nums): return False
        else: return True


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
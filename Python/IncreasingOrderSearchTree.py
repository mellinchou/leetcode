class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        nums=[]
        dummy=res=TreeNode()
        
        def dfs(node):
            if node==None: return
            nums.append(dfs(node.left))
            nums.append(node.val)
            nums.append(dfs(node.right))
            return
        
        def reconstructTree(res):
            for i in nums:
                if i!=None:
                    res.right=TreeNode(i)
                    res=res.right
        
        dfs(root)
        reconstructTree(res)
        return dummy.right
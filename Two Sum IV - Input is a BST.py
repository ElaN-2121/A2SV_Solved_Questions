# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        seen = set()
        
        def dfs(node):
            if not node:
                return False
            
            # Check if the complement exists in our set
            if (k - node.val) in seen:
                return True
            
            seen.add(node.val)
            
            # Continue searching left and right subtrees
            return dfs(node.left) or dfs(node.right)
            
        return dfs(root)

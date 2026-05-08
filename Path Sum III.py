# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        current_sum = 0
        count_path = 0

        def dfs(node, current_sum):
            nonlocal count_path

            if not node:
                return

            if current_sum + node.val == targetSum:
                count_path += 1

            new_sum = current_sum + node.val
            dfs(node.left, new_sum)
            dfs(node.right, new_sum)
        
        def traverse(node):
            if not node:
                return
                
            dfs(node, 0)
            traverse(node.left)
            traverse(node.right)
        
        traverse(root)
        return count_path

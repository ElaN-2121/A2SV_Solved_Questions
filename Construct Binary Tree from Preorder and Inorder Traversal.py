# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Build hashmap for quick index lookup in inorder
        inorder_map = {val: i for i, val in enumerate(inorder)}
        
        self.pre_idx = 0
        
        def build(left, right):
            if left > right:
                return None
            
            # Pick current root from preorder
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            
            root = TreeNode(root_val)
            
            # Find split point in inorder
            mid = inorder_map[root_val]
            
            # Build left subtree
            root.left = build(left, mid - 1)
            
            # Build right subtree
            root.right = build(mid + 1, right)
            
            return root
        
        return build(0, len(inorder) - 1)

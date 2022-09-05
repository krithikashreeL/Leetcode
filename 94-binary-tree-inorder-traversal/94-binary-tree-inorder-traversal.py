# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        
        def recursive_traversal(root,result):
            if root.left:
                recursive_traversal(root.left,result)
            result.append(root.val)
            if root.right:
                recursive_traversal(root.right,result)
            return result
        
        if root == None: return None
        
        return recursive_traversal(root,result)
        
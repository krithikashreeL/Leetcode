# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        result = []
        
        def recursive_postorder(root,result):
            if root.left:
                 recursive_postorder(root.left,result)
            if root.right:
                recursive_postorder(root.right,result)
            result.append(root.val)
            return result
        
        if root== None: return None
        return recursive_postorder(root,result)
    
        
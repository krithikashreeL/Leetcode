# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        result = []
        
        def recursive_preorder(root,result):
            if root:
                result.append(root.val)
            if root.left:
                recursive_preorder(root.left,result)
            if root.right:
                recursive_preorder(root.right,result)
            return result
        
        if root == None: return None
        return recursive_preorder(root,result)
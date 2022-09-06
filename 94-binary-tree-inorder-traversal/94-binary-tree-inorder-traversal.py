# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ## ITERATIVE APPROACH (Alternative for recursive approach is to use stack)
        result = []
        stack = []
        current = root
        while current or len(stack) != 0:
            while current:
                stack.append(current)
                current = current.left
        
            current = stack.pop()            
            result.append(current.val)
            current = current.right
            # print(current.val)
        return result
        
            
        
        
        ## RECURSIVE APPROACH
#         result = []
        
#         def recursive_traversal(root,result):
#             if root.left:
#                 recursive_traversal(root.left,result)
#             result.append(root.val)
#             if root.right:
#                 recursive_traversal(root.right,result)
#             return result
        
#         if root == None: return None
        
#         return recursive_traversal(root,result)
        
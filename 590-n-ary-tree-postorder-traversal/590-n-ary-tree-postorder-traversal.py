"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        result = []
        
        def recursive_postorder(root,result):
            if root:
                for child in root.children:
                    recursive_postorder(child,result)
                    result.append(child.val)
            
            
        recursive_postorder(root,result)
        if root: result.append(root.val)
        return result
        
#         # print(result)
#         return recursive_postorder(root,result)
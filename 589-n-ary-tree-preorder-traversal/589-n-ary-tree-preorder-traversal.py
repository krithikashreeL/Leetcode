"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        
        result = []
        
        def recursive_traversal(root,result):
            if root:
                result.append(root.val)
            
                for child in root.children:
                    recursive_traversal(child,result)
            return result
        
        return recursive_traversal(root,result)
        
        
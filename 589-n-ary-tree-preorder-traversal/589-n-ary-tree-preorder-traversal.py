"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        output = []
        
        def helper(root,output):
            if root!= None:
                output.append(root.val)
                if root and root.children:
                    for child in root.children:
                        helper(child,output)
                return output
        return helper(root,output)
        
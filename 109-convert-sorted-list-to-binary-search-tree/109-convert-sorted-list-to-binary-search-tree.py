# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        
        def BST(array):
            if array != []:
                mid_element = len(array) // 2
                # print(array[mid_element])
                root = TreeNode(array[mid_element])
                root.left = BST(array[:mid_element])
                root.right = BST(array[mid_element+1:])
                return root
            else:
                return None

        
        list_to_array = []
        while head:
            list_to_array.append(head.val)
            head = head.next
        return BST(list_to_array)
        
        
            
            
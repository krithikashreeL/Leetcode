# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack = []
        
        slow = fast = head
        
        
        #check for the mid of list
        while fast and fast.next:
            stack.append(slow.val)
            slow = slow.next
            fast = fast.next.next
        
        #reverse the second half        
        prev = next_node = None
        
        while slow:
            next_node = slow.next          
            
            slow.next = prev
            prev = slow
            slow = next_node
      
        left = head
        right = prev
        
        while right:
            if left.val != right.val:
                return False
            right = right.next
            left = left.next
        
        return True
        
            
        
        
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        if head == None: return None
        while head:
            if head.val == val:
                head = head.next
            else:
                break
            
        current = head
        
        while current:
            
            if current.next and current.next.val == val:
                current.next = current.next.next
                print(current.val)
            else:
                current = current.next
        
        
        return head
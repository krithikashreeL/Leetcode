# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        while head: # remove value from the begaining
            if head.val == val:
                head = head.next
            else:
                break
                
        newhead = head
        while head:
            if head.next and head.next.val == val: # seach for if the next will be deleted
                    head.next = head.next.next
            else:
                head = head.next
        
        return newhead
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
#         if head == None: return None
#         while (head != None and head.val == val):
#             head = head.next
#         pointer = head
        
#         while(pointer.next != None and pointer != None):
#             if pointer.next.val == val:
#                 pointer.next = pointer.next.next
#             else: pointer = pointer.next
        
#         return head
        
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
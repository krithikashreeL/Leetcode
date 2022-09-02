# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        sentinal = ListNode(0,head)
        predecesor = sentinal
        
        while head:
            
            if head.next and head.val == head.next.val:
                while head.next and  head.val == head.next.val:
                    head = head.next
                predecesor.next = head.next
            else:
                predecesor= predecesor.next
            head = head.next
        
        
        return sentinal.next
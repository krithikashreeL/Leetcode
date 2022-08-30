# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode(0)
        dummy = result
        carry = 0
        while l1 or l2:
            l1val = l1.val if l1 else 0
            l2val  = l2.val if l2 else 0
            val = l1val + l2val + carry
            carry = val // 10
            val = val % 10
            dummy.next = ListNode(val)
            dummy = dummy.next            
            l1 = l1.next if l1 else None
            l2 = l2.next  if l2 else None
        
        if carry != 0:
            dummy.next = ListNode(carry)
            dummy = dummy.next
        
        return result.next
            
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        fast = slow = head
        #get the middle element
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        first_half = slow
        
        #reverse second half
        previous = None        
        while slow:
            next_element = slow.next
            slow.next = previous
            previous = slow
            slow = next_element
        
        #second_half = previous
        # print(previous)
        while previous.next:
            next_of_first_half = head.next
            next_of_second_half = previous.next
            
            head.next = previous
            previous.next = next_of_first_half
            
            head = next_of_first_half
            previous = next_of_second_half
        
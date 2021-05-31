'''
This question is asked by Microsoft. Given a linked list, 
containing unique numbers, return whether or not it has a cycle.
Note: a cycle is a circular arrangement (i.e. one node points back to a previous node)
'''

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        
        slow = fast = head
        
        while (fast and fast.next)
            
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return True
        
        return False
        
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        
        seen = set()
        
        while head:
            if head in seen:
                return True
            seen.add(head)
            head = head.next
        return False
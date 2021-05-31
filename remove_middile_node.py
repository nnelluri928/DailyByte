'''
This question is asked by Amazon. 
Given a non-empty linked list, 
return the middle node of the list. If the linked list contains an 
even number of elements, return the node closer to the end.


1->2->3->null, return 2
1->2->3->4->null, return 3
1->null, return 1
'''

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        
        
        slow_pointer=head
        fast_pointer=head
        while(fast_pointer and fast_pointer.next):
            slow_pointer=slow_pointer.next
            fast_pointer=fast_pointer.next.next
        return slow_pointer
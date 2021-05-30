
'''
This question is asked by Google. Given a linked list and a value, 
remove all nodes containing the provided value, and return the resulting list.

Ex: Given the following linked lists and values...

1->2->3->null, value = 3, return 1->2->null
8->1->1->4->12->null, value = 1, return 8->4->12->null
7->12->2->9->null, value = 7, return 12->2->9->null
'''

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head == None:
            return head
        
        current = head
        while current.next != None:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
        
        return head if head.val != val else head.next   

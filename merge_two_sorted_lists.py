
'''
This question is asked by Apple. Given two sorted linked lists, merge them together in ascending order and return a reference to the merged list

Ex: Given the following lists...

list1 = 1->2->3, list2 = 4->5->6->null, return 1->2->3->4->5->6->null
list1 = 1->3->5, list2 = 2->4->6->null, return 1->2->3->4->5->6->null
list1 = 4->4->7, list2 = 1->5->6->null, return 1->4->4->5->6->7->null



'''

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        
        head = cur = ListNode()
        
        while l1 and l2:
            
            if l1.val <= l2.val:
                cur.next = l1
                l1 =l1.next
            
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
            
        
        if l1:
            cur.next = l1
            l1 = l1.next
        if l2:
            cur.next = l2
            l2 = l2.next
        
        return head.next
            


'''
Work in progress

'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1, l2):
        head = ListNode()
        lst = head

        while l1.next != None and l2.next != None:
            v1 = l1.val
            v2 = l2.val

            if v1 < v2:
                lst.val = v1
                lst.next = ListNode()
                lst = lst.next
                l1 = l1.next
            else:
                lst.val = v2
                lst.next = ListNode()
                lst = lst.next
                l2 = l2.next


lst1 = ListNode(1, ListNode(2, ListNode(4, None)))
lst2 = ListNode(1, ListNode(3, ListNode(5, None)))

head = lst2

while head.next != None:
    print(head.val)
    head = head.next
else:
    print(head.val)

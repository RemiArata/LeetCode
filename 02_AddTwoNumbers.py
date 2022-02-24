# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        self.tail = ListNode()
        self.head = self.tail
        self.cBit = 0

        while l1 is not None or l2 is not None:
            if l1 is None:
                l1 = ListNode(0, None)
            elif l2 is None:
                l2 = ListNode(0, None)
            self.tail.val = (l1.val + l2.val + self.cBit) % 10
            self.cBit = (l1.val + l2.val + self.cBit) // 10
            l1 = l1.next
            l2 = l2.next
            if l1 is None and l2 is None:
                break
            self.tail.next = ListNode()
            self.tail = self.tail.next
        
        if self.cBit != 0:
            self.tail.next = ListNode(self.cBit, None)
        
        return self.head

t1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, None)))))))
t2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, None))))

solve = Solution()
pnt = solve.addTwoNumbers(t1, t2)

while pnt is not None:
    print(pnt.val)
    pnt = pnt.next






class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        temp = ListNode()
        head = temp

        while l1 and l2:
            if l1.val < l2.val:
                head.next = l1
                l1 = l1.next
            else:
                head.next= l2
                l2 = l2.next
            head = head.next
        if l1 != None:
            head.next = l1
        else:
            head.next = l2
        return temp

def display(l: ListNode) -> None:
    while l.next != None:
        print(l.val)
        l = l.next
    else:
        print(l.val)


t1 = ListNode()
t2 = ListNode()

test = Solution()

blah = test.mergeTwoLists(t1, t2)
display(blah)
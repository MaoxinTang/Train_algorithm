def reverse(p,h,n):
    if h.next == None:
        h.next = p
        return h
    h.next=p
    return reverse(h,n,n.next)

class Solution(object):
    def reverseList(self, head):
        if not head or not head.next:
            return head
        return reverse(None,head,head.next)

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head:
            nextHead = head.next
            head.next, prev = prev, head
            head = nextHead
        return prev
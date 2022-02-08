class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None:
            return head
        elif head.next==None:
            return head
        t1,t2=head,head.next
        newhead=ListNode(-1)
        prev=newhead
        while t2:
            t1.next=t2.next
            t2.next=t1
            prev.next=t2
            prev=t1
            if t1.next==None:
                break
            t2=t1.next.next
            t1=t1.next
        return newhead.next
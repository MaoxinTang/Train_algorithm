class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if (fast==slow):
                meet = fast
                while head!=meet:
                    head=head.next
                    meet=meet.next
                return head
        return None
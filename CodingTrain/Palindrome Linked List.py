class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if(not head.next): return True
        
        p = head 
        odd = False
        fake = fast = slow = ListNode(0); fake.next = head
        
        while(fast.next):
            if(not fast.next.next):
                odd = True
                fast = fast.next

            else: fast = fast.next.next

            cur = p
            p = p.next
            cur.next = slow
            slow = cur

        if(odd):
            slow = slow.next

        while(p):
            if(p.val != slow.val):
                return False
            p = p.next
            slow = slow.next

        return True
class Solution(object):
    def oddEvenList(self, head):

        if not head: return head       
        odd = head
        even = firstEven = head.next
                
        while even and even.next:            
            odd.next = even.next
            odd = even.next
            even.next = odd.next
            even = odd.next      
        
        odd.next = firstEven

        return head
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head
        while(curr and curr.next!=None):
            ahead=curr.next  #check the node ahead and compare the value with current node value
            if ahead.val==curr.val:
                curr.next=curr.next.next 
            else:
                curr=curr.next
        return head
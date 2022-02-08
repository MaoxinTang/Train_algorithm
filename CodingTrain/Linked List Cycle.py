class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        while head is not None:
            
            # If the val is a boolean, then we know we have already traversed this node.
            if type(head.val) == bool:
                return True
            
            # Else, make the val of this node a boolean (could be 'False' or 'True'...doesn't matter)
            head.val = True
            
            # Go to the next node in the linked list
            head = head.next
        
        return False
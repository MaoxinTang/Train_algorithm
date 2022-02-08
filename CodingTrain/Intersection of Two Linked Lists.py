class Solution:

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        idsInA = set()
        while headA:
            idsInA.add(id(headA))
            headA = headA.next
        while headB:
            if id(headB) in idsInA:
                return headB
            headB = headB.next
        return None
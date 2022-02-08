class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        l=[]
        head=point=ListNode(0)
        for i in lists:
            while(i!=None):
                heappush(l,i.val)
                i=i.next
        print(l)
        while(len(l)>0):
            point.next=ListNode(heappop(l))
            point=point.next
        return head.next
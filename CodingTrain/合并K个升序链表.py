class Solution:
    def numerical_value (self, x):
        return math.inf if x is None else x.val

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        head_pre = ListNode()
        cur = head_pre
        priority_queue = []
        for i,v in enumerate(lists):
            heapq.heappush(priority_queue, (self.numerical_value(v),i,v))
        while priority_queue:
            _, i, min_node = heapq.heappop(priority_queue)
            if min_node is None:
                continue
            cur.next = min_node
            cur = cur.next
            heapq.heappush(priority_queue, (self.numerical_value(min_node.next), i, min_node.next))
        cur.next = None
        return head_pre.next

class Solution:
    def numerical_value(self, x):
        return math.inf if x is None else x.val

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        head_pre = ListNode()
        cur = head_pre
        lists = collections.deque(sorted(lists, key=self.numerical_value))
        lists_v = collections.deque(self.numerical_value(x) for x in lists)
        while lists:
            min_node = lists[0]
            lists.popleft()
            lists_v.popleft()
            if min_node is None:
                continue
            cur.next = min_node
            cur = cur.next
            if min_node.next:
                #bisect.insort_right(lists, min_node.next, key=self.numerical_value)
                index = bisect.bisect(lists_v, min_node.next.val)
                lists.insert(index, min_node.next)
                lists_v.insert(index, min_node.next.val)
        cur.next = None
        return head_pre.next
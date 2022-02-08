方法一：集合
如果发现节点已在集合内则说明存在环


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        s = set()
        while h2 != None and head.next != None:
            s.add(head)
            head = head.next
            if head in s:
                return True
        return False
方法二：双指针。
快慢指针，如果两个指针相遇则说明存在环


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        h1, h2 = head, head
        while h2 != None and h2.next != None:
            h2 = h2.next.next
            h1 = h1.next
            if h1 == h2:
                return True
        return False

作者：bluegreenred
链接：https://leetcode-cn.com/problems/linked-list-cycle/solution/141-huan-xing-lian-biao-python-ji-he-shu-152s/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
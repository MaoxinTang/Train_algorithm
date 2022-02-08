class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        arr=[]
        cur=head
        while cur:
            arr.append(cur.val)
            cur=cur.next
        def helper(left,right):
            if left>right:
                return None
            mid=(left+right)//2
            root=TreeNode(arr[mid])
            root.left=helper(left,mid-1)
            root.right=helper(mid+1,right)
            return root
        return helper(0,len(arr)-1)
        
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        d = float('inf')
        s = []
        if root == None:
            return 
        d = self.traverse(root,d,s)
        return d
    def traverse(self,root,d,s):
        if root.left != None:
            d = self.traverse(root.left,d,s)
        s.append(root.val)
        if len(s)>1:
            diff = s[-1]-s[-2]
            if diff < d:
                d = diff
        if root.right != None:
            d = self.traverse(root.right,d,s) 
        return d
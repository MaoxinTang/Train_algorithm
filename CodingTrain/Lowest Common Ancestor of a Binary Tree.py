class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def contains(node):
            '''
            returns True if the subtree rooted at node
            contains either p or q
            '''
            if not node:
                return False
            n = node == p or node == q
            l = contains(node.left)
            r = contains(node.right)
            if n+l+r == 2:
                self.ret = node
            return n or l or r
        
        self.ret = root
        contains(root)
        return self.ret
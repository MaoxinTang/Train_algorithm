class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def dfs(root,par):
            if not root:
                return 0
            l,r = dfs(root.left,root),dfs(root.right,root)
            if par and not root.left and not root.right and root == par.left:
                return root.val + l + r
            return l + r
        return dfs(root,None)
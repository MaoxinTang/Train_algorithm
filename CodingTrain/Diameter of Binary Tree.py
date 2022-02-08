class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        dia=0
        def dfs(root):
            if not root:
                return 0
            right_height=dfs(root.right)
            left_height=dfs(root.left)
            nonlocal dia
            dia=max(dia,right_height+left_height)
            return 1+max(right_height,left_height)
        
        dfs(root)
        return dia
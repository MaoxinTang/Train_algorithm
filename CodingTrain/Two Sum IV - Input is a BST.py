class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        
        num_set = set()
        
        def dfs(node):
            nonlocal num_set
            if not node:
                return False
            if node.val in num_set:
                return True
            num_set.add(k - node.val)
            return dfs(node.left) or dfs(node.right)
        
        return dfs(root)
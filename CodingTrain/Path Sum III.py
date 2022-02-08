class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        ans = [0]
        
        def dfs(node, curr_sum):
            if not node: return
            curr_sum += node.val
            if (curr_sum - sum) in mapping:
                ans[0] += mapping[curr_sum - sum]
            mapping[curr_sum] += 1
            dfs(node.left, curr_sum)
            dfs(node.right, curr_sum)
            mapping[curr_sum] -= 1
            
        mapping = defaultdict(int)
        mapping[0] = 1
        dfs(root, 0)
        return ans[0]
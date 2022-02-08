class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if root is None:
            return []
        queue = [root]
        output = []
        while queue:
            temp = []
            for i in range(len(queue)):
                curr = queue.pop(0)
                temp.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            val = float(sum(temp)/len(temp))
            output.append(val)
        return output
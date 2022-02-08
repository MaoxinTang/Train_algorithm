class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        
        to_remove, queue, forest = set(to_delete), deque([(root, True)]), []
        while queue:
            node, flag = queue.pop()
            if node.right:
                queue.append((node.right, node.val in to_remove))
                if node.right.val in to_remove: node.right = None 
            if node.left:
                queue.append((node.left, node.val in to_remove))
                if node.left.val in to_remove: node.left = None
            if node.val not in to_remove and flag:
                forest.append(node)
        return forest
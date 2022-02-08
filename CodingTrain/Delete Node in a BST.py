class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        left = root.left
        right = root.right
        if root.val == key:
            if right is None:
                root = left
                return root
            if left is None:
                root = right
                return root
            left_r = left
            while left_r.right:
                left_r = left_r.right
            left_r.right = right
            root = left
            return root
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
        return root
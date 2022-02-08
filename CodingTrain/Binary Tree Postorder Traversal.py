class Solution:
    def traversal(self, root, postorder):
        if root:
            self.traversal(root.left, postorder)
            self.traversal(root.right, postorder)
            postorder.append(root.val)
            
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        postorder = []
        self.traversal(root, postorder)
        return postorder
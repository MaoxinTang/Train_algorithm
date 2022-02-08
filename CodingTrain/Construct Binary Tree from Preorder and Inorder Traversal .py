class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not inorder:
            return None
        root=TreeNode(preorder.pop(0))
        root_idx=inorder.index(root.val)
        root.left=self.buildTree(preorder,inorder[:root_idx])
        root.right=self.buildTree(preorder,inorder[root_idx+1:])
        return root
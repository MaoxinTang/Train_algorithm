class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder:
            return
        
        r=postorder.pop() 
        root=TreeNode(r) 
        i=inorder.index(r) 
        
        root.right=self.buildTree(inorder[i+1:],postorder) 
        root.left=self.buildTree(inorder[:i],postorder) 
        return root
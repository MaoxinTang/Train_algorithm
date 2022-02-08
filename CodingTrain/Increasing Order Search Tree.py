class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        ans = self.bst = TreeNode(None,None,None)
        self.dfs(root)
        
        return ans.right
    
    def dfs(self,node):
        if node == None:
            return
        
        
        self.dfs(node.left)
        #print(node.val)
        
        
        self.bst.right = TreeNode(node.val,None,None)
        
        self.bst = self.bst.right
        #print(self.bst.right.val)
    
        
        self.dfs(node.right)
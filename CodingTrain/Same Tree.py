class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(p=p, q=q):
#if one value is null return false
            if(p and not q):
                return False
            elif(q and not p):
                return False
#if both are null return true
            elif not (p and q):
                return True
#values are equal call the function on left and right
            if(p.val==q.val):
                #return true if both left and right are equal
                return(dfs(p.left, q.left) and dfs(p.right, q.right))
            else:
#if they aren't equal return false
                return False
            
        return(dfs())
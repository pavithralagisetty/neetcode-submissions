# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        l=[]
        def dfs(root):
            if root==None:
                return
            dfs(root.left)
            l.append(root.val)
            dfs(root.right)
        dfs(root)
        s=sorted(l)
        for i in range(len(l)):
            if l[i]!=s[i]:
                a=l[i]
                b=s[i]
                break
        print(l)
        print(a,b)
        def dfs1(root):
            if root==None:
                return
            if root.val==a:
                root.val=b
            elif root.val==b:
                root.val=a
            dfs1(root.left)
            dfs1(root.right)
        dfs1(root)

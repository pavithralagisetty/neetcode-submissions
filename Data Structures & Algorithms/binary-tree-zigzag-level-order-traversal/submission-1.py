# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q=deque()
        q.append(root)
        res=[]
        flag=0
        if not root:
            return []
        while q:
            level=[]
            if flag==0:
                flag=1
            else:
                flag=0
            for _ in range(len(q)):
                node=q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if flag==1:
                res.append(level)
            else:
                res.append(level[::-1])
        return res

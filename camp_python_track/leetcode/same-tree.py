# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ans = True
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p and q:
            # print("both of them exiss",p.val,q.val)
            if p.val!=q.val:
                return False
            left_output = self.isSameTree(p.left,q.left)
            if not left_output:
                return left_output
            right_output = self.isSameTree(p.right,q.right)
            if not right_output:
                return right_output
        else:
            if not (p==None and q==None):
                return False
            else:
                return True
        return True
            
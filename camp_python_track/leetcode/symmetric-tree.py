# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def mirror(ls,rs):
            if rs and ls:
                # print("this is the right,left ",rs.val==ls.val)
                if ls.val == rs.val:
                    ans1 = mirror(ls.left,rs.right)
                    if not ans1:
                        return ans1
                    ans2 = mirror(ls.right,rs.left)
                    if not ans2:
                        return ans2
                else:
                    return False
            else:
                if  (rs and not ls) or (ls and not rs):
                    return False
            return True
    
        if root:
            left_side = root.left
            right_side = root.right
            return mirror(left_side,right_side)
        return True


        
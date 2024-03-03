# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans  =[]
        sm = 0
        def find_path(node,depth,val):
            nonlocal sm
            # print(val,depth,ans)
            if node:
                val*=10
                val+=node.val
                if  (not node.right and not node.left):
                    ans.append(val)
                    sm+=val
                else:
                    find_path(node.left,depth+1,val)
                    find_path(node.right,depth+1,val)
                
        find_path(root,0,0)
        # print(ans)
        # print(sm)
        return sm

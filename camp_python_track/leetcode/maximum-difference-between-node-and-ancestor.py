# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    mx =0
    mn = 10**5
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        max_dif = 0
        def max_diff_anc(node,max_anc,min_anc):
            nonlocal max_dif
            if node:
                dif = max(abs(node.val-max_anc),abs(node.val-min_anc))
                max_anc = max(node.val,max_anc)
                min_anc = min(node.val,min_anc)
                if max_dif<dif:
                    max_dif=dif
                max_diff_anc(node.left,max_anc,min_anc)
                max_diff_anc(node.right,max_anc,min_anc)
        max_diff_anc(root,root.val,root.val)
        return max_dif
        
        


        
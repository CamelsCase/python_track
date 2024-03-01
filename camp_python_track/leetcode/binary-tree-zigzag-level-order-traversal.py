# class TreeNode:
#     def init(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        dt = defaultdict(list)
        def store_level(node,level):
            if node:
                dt[level].append(node.val)
                store_level(node.left,level+1)
                store_level(node.right,level+1)
                
        store_level(root,0)
        ans = []
       
        for i in dt:
            if i%2==0:
                ans.append(dt[i])
            else:
                ans.append(dt[i][::-1])
        return ans
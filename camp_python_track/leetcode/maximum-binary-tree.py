# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def generate(left,right):
            # print(left,right)
            if left<=right:
                ind = nums.index(max(nums[left:right+1]))
                # print("this is the index0",ind)
                temp = TreeNode(nums[ind])
                temp.left = generate(left,ind-1)
                temp.right = generate(ind+1,right)
                return temp
        return generate(0,len(nums)-1)
        
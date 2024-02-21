class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def choose(left,right):
            if left==right:
                return nums[right]
            l = nums[left]-choose(left+1,right)
            r = nums[right]-choose(left,right-1)
            # print(l,r)
            return max(l,r)
        return choose(0,len(nums)-1)>=0



















        # def choose(player,p1_score,p2_score,st,en):
        #     print(p1_score,p2_score,st,en,player)
        #     #if the score of selecting the two paths leads to lossing.try reselecting a path that do not lead to this path
        #     if player:
        #         #selecting the first element
        #         path_1=nums[st]
        #         st+=1
        #         print("thsi is the path 1 sum",player,path_1)
        #         if st==en:
        #             return False
        #         p1_score+=path_1
        #         choose(not player,p1_score,p2_score,st,en)
        #         #selecting the second path
        #         st-=1
        #         path_2 = nums[en]
        #         p1_score+=path_2-path_1
        #         print("thsi is the path 2 sum",player,path_2)
        #         en-=1
        #         if st==en:
        #             return False
        #         choose(not player,p1_score,p2_score,st,en)
        #     else:
        #         #selecting the first element
        #         path_1=nums[st]
        #         st+=1
        #         p2_score+=path_1
        #         print("thsi is the path 1 sum",player,path_1)
        #         if st==en:
        #             return False
        #         choose(not player,p1_score,p2_score,st,en)
        #         #selecting the second path
        #         st-=1
        #         path_2 = nums[en]
        #         p2_score+=path_2-path_1
        #         print("thsi is the path 1 sum",player,path_2)
        #         en-=1
        #         if st==en:
        #             return False
        #         choose(not player,p1_score,p2_score,st,en)
            
            

                
        #     #if there is not any path for you to select you will lose

        return  choose(True,0,0,0,len(nums)-1)
        
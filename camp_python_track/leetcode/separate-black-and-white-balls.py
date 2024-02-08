class Solution:
    def minimumSteps(self, s: str) -> int:
        zeros = s.count("0")
        ones = s.count("1")

        zeros_to_the_right= []
        for i in s:
            if i=="0":
                zeros_to_the_right.append(0)
                zeros-=1
            else:
                zeros_to_the_right.append(zeros)
                ones-=1
        cnt = 0
        for i in zeros_to_the_right:
            cnt+=i
        return cnt
class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        n1 = (num-3)//3
        return [n1,n1+1,n1+2] if num%3==0 else []
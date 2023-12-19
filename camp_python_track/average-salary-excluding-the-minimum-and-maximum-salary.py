class Solution:
    def average(self, salary: List[int]) -> float:
        leng = len(salary)
        salary.sort()
        x = sum(salary[1:leng-1])
        return x/(leng-2)
        
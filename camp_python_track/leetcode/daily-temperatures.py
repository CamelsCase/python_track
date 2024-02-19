class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        days_to_wait = defaultdict(lambda:0)
        for ind,tem  in enumerate(temperatures):
            if not stack:
                stack.append((ind,tem))
            else:
                if stack[-1][1]<tem:
                    while stack and stack[-1][1]<tem:
                        val = stack.pop()
                        days_to_wait[val[0]] = ind-val[0]
                stack.append((ind,tem))
        return [days_to_wait[i] for i in range(len(temperatures))]
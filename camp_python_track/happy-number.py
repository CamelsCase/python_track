class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(num):
            result = 0
            while num > 0:
                digit = num % 10
                result += digit ** 2
                num //= 10
            return result
        
        slow = n
        fast = get_next(n)
        while fast != 1 and slow != fast:
            slow = get_next(slow)
            fast = get_next(get_next(fast))
        return fast == 1
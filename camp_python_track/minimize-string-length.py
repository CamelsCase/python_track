class Solution:
    def minimizedStringLength(self, s: str) -> int:
        return len(set([i for i in s]))
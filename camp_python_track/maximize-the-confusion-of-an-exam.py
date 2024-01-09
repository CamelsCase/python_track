class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        maxConsecutive = 0
        left = 0
        right = 0
        freq = {'T': 0, 'F': 0}
        n = len(answerKey)

        while right < n:
            freq[answerKey[right]] += 1
            maxFreq = max(freq.values())

            if (right - left + 1) - maxFreq > k:
                freq[answerKey[left]] -= 1
                left += 1

            maxConsecutive = max(maxConsecutive, right - left + 1)
            right += 1

        return maxConsecutive

import sys
sys.set_int_max_str_digits(10000000)
class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        freq = Counter(nums)
        ky  = list(freq.keys())
        ky.sort(reverse = True)
        out = 0
        cum  = 0
        for i in ky[:len(ky)-1]:
            out+=cum+freq[i]
            cum+=freq[i]
        return out
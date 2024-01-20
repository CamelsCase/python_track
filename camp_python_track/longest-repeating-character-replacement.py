class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        st = 0
        en = 0
        cnt = {}
        mx = 0
        while en < len(s):
            if s[en] not in cnt:
                cnt[s[en]] = 1
            else:
                cnt[s[en]] += 1

            while (en - st + 1) - max(cnt.values()) > k:
                cnt[s[st]] -= 1
                st += 1

            mx = max(mx, en - st + 1)
            en += 1

        return mx
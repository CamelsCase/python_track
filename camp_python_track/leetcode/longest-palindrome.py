class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = Counter(s).most_common()
        take_odds = True
        leng = 0
        for i in freq:
            if  i[1]%2==1:
                if take_odds:
                    leng+=i[1]
                    take_odds = False
                else:
                    leng+=i[1]-1
            else:
                leng+=i[1]
        return leng

            

        
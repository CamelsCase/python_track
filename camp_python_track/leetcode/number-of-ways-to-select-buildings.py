class Solution:
    def numberOfWays(self, s: str) -> int:
        leng = len(s)
        z_o  = defaultdict(lambda:Counter())
        z_o[-1] = {"0":0,"1":0}
        z_cnt = s.count("0")
        o_cnt = s.count("1")
        cnt = 0
        for i,v in enumerate(s):
            z_o[i] = z_o[i-1].copy()
            z_o[i][v]+=1
            if v=="0":
                cnt += z_o[i]["1"]*(o_cnt - z_o[i]["1"])
            else:
                cnt += z_o[i]["0"]*(z_cnt - z_o[i]["0"])
            # print(cnt)
        

        return cnt



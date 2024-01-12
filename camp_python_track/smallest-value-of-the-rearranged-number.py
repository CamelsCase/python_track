class Solution:
    def smallestNumber(self, num: int) -> int:
        snum = [i for i in str(num)]
        sign = "+"
        if snum[0]=="-":
            sign = "-"
            snum = snum[1:]
            snum.sort(reverse = True)
        else:
            snum.sort()
        # print(snum)
        if snum[0]=="0":
            for i in range(1,len(snum)):
                if snum[i]!="0":
                    snum[0],snum[i] = snum[i],snum[0]
                    break
        return int(sign+"".join(snum))

            
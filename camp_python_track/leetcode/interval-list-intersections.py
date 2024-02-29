class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        pt1 = 0
        pt2 = 0
        a1_leng = len(firstList)
        a2_leng = len(secondList)
        out = []
        while pt1<a1_leng and pt2<a2_leng:
            x = []
            # print(pt1,pt2,out)
            if firstList[pt1][0]<secondList[pt2][0]:
                if firstList[pt1][0]<=secondList[pt2][0]<=firstList[pt1][1]:
                    x.append(max(firstList[pt1][0],secondList[pt2][0]))
                    x.append(min(firstList[pt1][1],secondList[pt2][1]))
            elif firstList[pt1][0]>=secondList[pt2][0]:
                if secondList[pt2][0]<=firstList[pt1][0]<=secondList[pt2][1]:
                    x.append(max(firstList[pt1][0],secondList[pt2][0]))
                    x.append(min(firstList[pt1][1],secondList[pt2][1]))
            if secondList[pt2][1]>firstList[pt1][1]:
                pt1+=1
            else:
                pt2+=1
            if len(x)==2:
                out.append(x)
                # print(out)
        return out



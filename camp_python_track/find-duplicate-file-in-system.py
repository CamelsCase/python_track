class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        cnt = defaultdict(list)
        for i in paths:
            fl = i.split(" ")
            path = fl[0]
            files = fl[1:]
            for f in files:
                content = f.split('(')
                fln = content[0]
                cntnt = content[1][:-1]
                cnt[cntnt].append(path+"/"+fln)
        st = []
        for i in cnt.values():
            if len(i)>1:
                st.append(list(i))
        return st
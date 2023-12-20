class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows = ["qwertyuiop","asdfghjkl","zxcvbnm"]
        # print(words)
        out = []
        for i in range(len(words)):
            x = words[i].lower()
            for j in  rows:
                # print(words[i].lower(),j)
                # print(set(x),"--->",set(j),"--->",set(x)&set(j),"--->",set(x)&set(j) == set(x))
                if set(x)&set(j) != set() and set(x)&set(j) != set(x):
                    break
                elif set(x)&set(j) == set():
                    pass
                else:
                    out.append(words[i])
                    break
        return out
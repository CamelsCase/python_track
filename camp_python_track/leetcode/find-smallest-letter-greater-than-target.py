class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        st = 0
        leng = len(letters)
        en = leng-1
        found = None
        while st<=en:
            mid = (st+en)//2
            if letters[mid]<=target:
                st = mid+1
            elif letters[mid]>target:
                found = letters[mid]
                en= mid-1
        return found if found else letters[0]
                
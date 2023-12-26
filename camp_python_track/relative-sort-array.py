class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        out = []
        for i in arr2:
            for j in range(arr1.count(i)):
                out.append(i)
        sortable = []
        for i in set(arr1).difference(set(arr2)):
            for j in range(arr1.count(i)):
                sortable.append(i)
        out.extend(sorted(sortable))
        return out
def custom_alphabet_sort(words, alphabet):
    wd = words.copy()
    def custom_key(wd):
        return [alphabet.index(c) for c in wd]

    wd.sort(key=custom_key)
    return wd
    

class Solution:
    def isAlienSorted(self, words: list[str], order: str) -> bool:
        t1 = custom_alphabet_sort(words, order)
        print(t1,words)
        return t1==words
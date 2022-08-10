class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        length = len(pref)
        count = 0
        for word in words:
            if pref == word[:length]:
                count += 1
        return count
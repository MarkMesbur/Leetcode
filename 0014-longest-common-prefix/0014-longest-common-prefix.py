class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp = ""
        strs.sort()
        first = strs[0]
        last = strs[-1]
        for letter in range(min(len(first), len(last))):
            if first[letter] != last[letter]:
                return lcp
            lcp += first[letter]
        return lcp
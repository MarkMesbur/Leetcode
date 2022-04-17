class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        long = ""
        c = ""
        for i in range(0,len(strs[0])):
            c = strs[0][i]   
            for j in range(1,len(strs)):
                if i==len(strs[j]) or c != strs[j][i]:
                       return long
            long += c
        return long
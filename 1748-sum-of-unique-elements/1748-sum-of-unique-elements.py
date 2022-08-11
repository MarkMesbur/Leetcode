from collections import Counter
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        n = Counter(nums)
        res = 0
        for i in n:
            if n[i]==1:
                res+=i
        return res
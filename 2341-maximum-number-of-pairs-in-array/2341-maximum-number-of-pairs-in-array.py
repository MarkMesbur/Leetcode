from collections import Counter
class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        counts = Counter(nums)
        pairs = [0,0]
        for key, value in counts.items():
            pairs[0] += value // 2 
            pairs[1] += value % 2
        return pairs
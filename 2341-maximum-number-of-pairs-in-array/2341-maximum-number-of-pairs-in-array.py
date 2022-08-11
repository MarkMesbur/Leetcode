from collections import Counter
class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        counts = Counter(nums)
        pairs = [0,0]
        for key, value in counts.items():
            if value > 1:
                pairs[0] += value // 2 
            if value % 2 == 1:
                pairs[1] += 1
        return pairs
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        hsh = {}
        sumof = 0
        for num in nums:
            if num in hsh.keys():
                hsh[num] += 1
            else:
                hsh[num] = 1
                    

        for key, value in hsh.items():
            if value == 1: 
                sumof += key
        return sumof
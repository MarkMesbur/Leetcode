class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        length = len(arr)
        odd_sum = 0
        
        for i in range(1, length + 1, 2):
            for j in range(length - i + 1):
                odd_sum += sum(arr[j:j+i])
        return odd_sum
       
            
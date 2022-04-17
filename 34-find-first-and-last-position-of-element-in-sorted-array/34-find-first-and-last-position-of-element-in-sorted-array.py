class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums)-1
        mid = int(right/2)
        ans = []
        while left < right:
            mid = int((left + right)/2)
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid 
    
        if not nums:
            return [-1,-1]
        elif nums[left] != target:
            return [-1,-1]
        ans.append(left)
        try:
            while nums[left] == target:
                left += 1
        except IndexError:
               pass
        ans.append(left-1)
        return ans
                
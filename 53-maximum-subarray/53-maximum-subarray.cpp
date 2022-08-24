#include <numeric>

class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int n = nums.size();
        vector<int> dp(n);
        int maxi = INT_MIN;
        dp[0] = nums[0];
        
        for (int i = 1; i < n; i++){
            dp[i] = max(nums[i], dp[i-1] + nums[i]);}
        
        int max = *max_element(dp.begin(), dp.end());
        
        return max;
    }
};
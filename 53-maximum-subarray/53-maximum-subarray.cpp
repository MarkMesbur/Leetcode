class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        if (nums.empty()) return INT_MIN;
        
        int currsum = nums[0];
        int largsum = nums[0];
        
        for (int i = 1; i < nums.size(); i++){
            currsum = max(currsum+nums[i], nums[i]);
            largsum = max(currsum, largsum);
        }
        return largsum;
        
    }
};
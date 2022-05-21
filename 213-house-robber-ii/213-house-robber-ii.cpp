class Solution {
public:
    int rob(vector<int>& nums) {
        int n = nums.size();
        if(nums.empty()) return 0;
        if(n == 1) return nums[0];
        if(n == 2 ) return max(nums[0],nums[1]);
            
        
        vector<int> start1(nums.begin(), nums.end()-1);
        vector<int> start2(nums.begin()+1, nums.end());
        
        return max(robbed(start1),robbed(start2));
    }
    
    int robbed(vector<int> v){
        int n = v.size();
        vector<int> dp(n);
        dp[0] = v[0];
        dp[1] = max(v[1],dp[0]);

        for (int i = 2; i < n; i++){
            dp[i] = max(v[i] + dp[i-2], dp[i-1]);
            }   
        return dp[n-1];}
};
class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        set<vector<int> > set;
        sort(nums.begin(), nums.end());
        int len = nums.size();
        long long sum_of = 0;

            for (int i = 0; i < len - 3; i++){
                for (int j = i + 1; j < len - 2; j++){
                    int k = j + 1;
                    int l = len - 1;
                    while (k < l){
                        sum_of = static_cast<long long>(nums[i]) + nums[j] + nums[k] + nums[l];
                        if (sum_of == target){
                            vector<int> temp = {nums[i], nums[j], nums[k], nums[l]};
                            set.insert(temp);
                            k += 1;}
                        else if (sum_of > target){
                            l -= 1;}
                        else {k += 1;}
                    }    
                }
            }
        vector<vector<int>> ans(set.begin(), set.end());
        return ans;
    }
};
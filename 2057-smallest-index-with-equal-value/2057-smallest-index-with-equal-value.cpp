class Solution {
public:
    int smallestEqual(vector<int>& nums) {
        int i = 0;
        int n = nums.size();
        for (i = 0; i < n; i++){
            if (i % 10 == nums[i]){return i;}
        }
        return -1;
    }
};
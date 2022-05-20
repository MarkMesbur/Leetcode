class Solution {
public:
    int climbStairs(int n) {
        if (n == 1){return 1;}
        else if (n == 2){return 2;}
        int prev =  1, curr = 2;
        int step = 0;
        for (int i = 2; i < n; i++){
            step = prev + curr;
            prev = curr;
            curr = step;
            
        }
        return step;
    }
};
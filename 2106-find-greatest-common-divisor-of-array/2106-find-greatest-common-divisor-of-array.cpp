class Solution {
public:
    int findGCD(vector<int>& nums) {
        using namespace std;
        int mn = *min_element(nums.begin(), nums.end());
        int mx = *max_element(nums.begin(), nums.end());

        
        for (int i = mn; i > 1; i--){
            if ((mx % i == 0) && (mn % i == 0)) return i;
        }
        return 1;
    }

};
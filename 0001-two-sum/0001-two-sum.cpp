class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> hashmap;
        
        for (int i = 0; i < nums.size(); i++) {
            hashmap[nums[i]] = i;
        }
        
        for (int i = 0; i < nums.size(); i++) {
            int diff = target - nums[i];
            
            if (hashmap.count(diff) && hashmap.at(diff) != i) {
                return {i, hashmap.at(diff)}; 
            }
        }
        
        return {-1, -1};
    }
};
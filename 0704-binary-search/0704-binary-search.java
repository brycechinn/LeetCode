class Solution {
    public int search(int[] nums, int target) {
        int l = 0;
        int r = nums.length - 1;
        
        while (l <= r) {
            int m = (l + r) / 2;
            int num = nums[m];
            
            if (num < target) {
                l = m + 1;
            } else if (num > target) {
                r = m - 1;
            } else {
                return m;
            }
        }
        
        return -1;
    }
}
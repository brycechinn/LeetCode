class Solution {
    public int search(int[] nums, int target) {
        // approach: compare m to left sorted portion or right sorted portion
        
        int l = 0;
        int r = nums.length - 1;
        
        while (l <= r) {
            int m = (l + r) / 2;
            
            int mid = nums[m];
            int left = nums[l];
            int right = nums[r];
            
            if (mid == target) {
                return m;
            }
            
            if (left <= mid) { // left sorted portion
                if (target > mid || target < left) {
                    l = m + 1;
                } else {
                    r = m - 1;
                }
            } else { // right sorted portion
                if (target < mid || target > right) {
                    r = m - 1;
                } else {
                    l = m + 1;
                }
            }
        }
        
        return -1;
    }
}
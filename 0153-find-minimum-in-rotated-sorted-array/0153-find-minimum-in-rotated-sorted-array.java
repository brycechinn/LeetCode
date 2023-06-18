class Solution {
    public int findMin(int[] nums) {
        int l = 0;
        int r = nums.length - 1;
        int min = nums[0];
        
        while (l <= r) {
            int m = (l + r) / 2;
            
            min = Math.min(min, nums[m]);
            
            if (nums[m] > nums[r]) {
                l = m + 1;
            } else if (nums[m] < nums[r]) {
                r = m - 1;
            } else {
                return min;
            }
        }
        
        return min;
    }
}
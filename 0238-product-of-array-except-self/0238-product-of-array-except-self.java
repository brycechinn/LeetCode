class Solution {
    public int[] productExceptSelf(int[] nums) {
        // approach 1: prefix and postfix arrays
        
        /*
        int[] pres = new int[nums.length];
        int[] posts = new int[nums.length];
        
        int pre = 1;
        int post = 1;
        
        // store prefixes
        for (int i = 0; i < nums.length; i++) {
            pres[i] = pre * nums[i];
            pre *= nums[i];
        }
        
        // store postfixes
        for (int i = nums.length - 1; i >= 0; i--) {
            posts[i] = post * nums[i];
            post *= nums[i];
        }
        
        for (int i = 0; i < nums.length; i++) {
            if (i == 0) {
                nums[i] = 1 * posts[i + 1];
            } else if (i == nums.length - 1) {
                nums[i] = pres[i - 1] * 1;
            } else {
                nums[i] = pres[i - 1] * posts[i + 1];
            }
        }
        
        return nums;
        */
        
        // approach 2: O(1) memory solution
        
        int[] res = new int[nums.length];
        
        int pre = 1;
        int post = 1;
        
        for (int i = 0; i < nums.length; i++) {
            res[i] = pre;
            pre *= nums[i];
        }
        
        for (int i = nums.length - 1; i >= 0; i--) {
            res[i] *= post;
            post *= nums[i];
        }
        
        return res;
    }
}
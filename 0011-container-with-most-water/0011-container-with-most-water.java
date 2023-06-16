class Solution {
    public int maxArea(int[] height) {
        // approach: two pointers
        
        int result = 0;
        
        int l = 0;
        int r = height.length - 1;
        
        while (l < r) {
            int area = (r - l) * Math.min(height[l], height[r]);
            result = Math.max(result, area);
            
            if (height[r] < height[l]) {
                r--;
            } else {
                l++;
            }
        }
        
        return result;
    }
}
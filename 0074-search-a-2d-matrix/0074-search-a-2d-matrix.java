class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        // approach: two binary searches, one to find row and one to find num within row
        
        // binary search to find row
        int l = 0;
        int r = matrix.length - 1;
        int m = 0;
        
        while (l <= r) {
            m = (l + r) / 2;
            
            if (target < matrix[m][0]) {
                r = m - 1;
            } else if (target > matrix[m][matrix[m].length - 1]) {
                l = m + 1;
            } else { // target is in row
                break;
            }
        }
        
        System.out.println("row: " + m);
        int[] nums = matrix[m];
        
        // binary search to find num
        l = 0;
        r = nums.length - 1;
        
        while (l <= r) {
            int mid = (l + r) / 2;
            
            if (target < nums[mid]) {
                r = mid - 1;
            } else if (target > nums[mid]) {
                l = mid + 1;
            } else { // target found
                return true;
            }
        }
        
        return false;
    }
}
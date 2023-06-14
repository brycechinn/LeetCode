class Solution {
    public boolean isPalindrome(String s) {
        // approach: two pointers
        
        int l = 0;
        int r = s.length() - 1;
        
        while (l < r) {
            char start = s.charAt(l);
            char end = s.charAt(r);
            
            if (!Character.isLetterOrDigit(start)) {
                l++;
                continue;
            }
            
            if (!Character.isLetterOrDigit(end)) {
                r--;
                continue;
            }
            
            if (Character.toLowerCase(start) != Character.toLowerCase(end)) {
                return false;
            }
            
            l++;
            r--;
        }
        
        return true;
    }
}
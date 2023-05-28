class Solution {
    public boolean isPalindrome(String s) {
        // approach: two pointers, compare l and r
        
        int l = 0;
        int r = s.length() - 1;
        
        while (l <= r) {
            while (l < s.length() && !Character.isLetter(s.charAt(l)) && 
                   !Character.isDigit(s.charAt(l))) {
                l++;
            }
            
            while (r >= 0 && !Character.isLetter(s.charAt(r)) && 
                   !Character.isDigit(s.charAt(r))) {
                r--;
            }
            
            if (l < s.length() && r >= 0 && Character.toLowerCase(s.charAt(l)) != 
                Character.toLowerCase(s.charAt(r))) {
                return false;
            }
            
            l++;
            r--;
        }
        
        return true;
    }
}
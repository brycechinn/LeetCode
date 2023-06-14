class Solution {
    public boolean isPalindrome(String s) {
        int l = 0;
        int r = s.length() - 1;
        
        while (l < r) {
            while (l < s.length() && !isAlphanumeric(s.charAt(l))) {
                l++;
            }
            
            while (r >= 0 && !isAlphanumeric(s.charAt(r))) {
                r--;
            }
            
            if (l >= r) {
                break;
            }
            
            if (Character.toLowerCase(s.charAt(l)) != Character.toLowerCase(s.charAt(r))) {
                return false;
            }
            
            l++;
            r--;
        }
        
        return true;
    }
    
    private boolean isAlphanumeric(char c) {
        return Character.isLetter(c) || Character.isDigit(c); 
    }
}
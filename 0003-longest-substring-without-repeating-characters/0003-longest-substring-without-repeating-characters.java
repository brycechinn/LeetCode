class Solution {
    public int lengthOfLongestSubstring(String s) {
        // approach: hashset to store nums in current valid window
        
        int result = 0;
        int l = 0;
        
        Set<Character> window = new HashSet<>();
        
        for (int r = 0; r < s.length(); r++) {
            char c = s.charAt(r);
            
            while (window.contains(c)) {
                window.remove(s.charAt(l));
                l++;
            }
            
            window.add(c);
            result = Math.max(result, window.size());
        }
        
        return result;
    }
}
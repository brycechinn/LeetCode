class Solution {
    public int characterReplacement(String s, int k) {        
        // approach: array of char values 0-26 : frequency in current window
        
        int result = 0;
        int[] counts = new int[26];
        
        // window size: r - l + 1
        int l = 0;
        for (int r = 0; r < s.length(); r++) {
            counts[s.charAt(r) - 'A']++;
            
            // get max freq in current window
            int max = 0;
            for (int num : counts) {
                max = Math.max(max, num);
            }
            
            while ((r - l + 1) - max > k) {        
                counts[s.charAt(l) - 'A']--;
                l++;
                
                // potential new max
                for (int num : counts) {
                    max = Math.max(max, num);
                }
            } 
            
            result = Math.max(result, r - l + 1);
        }
        
        return result;
    }
}
class Solution {
    public int characterReplacement(String s, int k) {
        // approach: hashmap of char : frequency in current window
        
        int result = 0;
        Map<Character, Integer> hashmap = new HashMap<>();
        
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            
            if (!hashmap.containsKey(c)) {
                hashmap.put(c, 0);
            }
        }
        
        // window size: r - l + 1
        int l = 0;
        for (int r = 0; r < s.length(); r++) {
            hashmap.put(s.charAt(r), hashmap.get(s.charAt(r)) + 1);
            
            // get max freq in current window
            int max = 0;
            for (int num : hashmap.values()) {
                max = Math.max(max, num);
            }
            
            while ((r - l + 1) - max > k) {        
                hashmap.put(s.charAt(l), hashmap.get(s.charAt(l)) - 1);
                l++;
                
                // potential new max
                for (int num : hashmap.values()) {
                    max = Math.max(max, num);
                }
            } 
            
            result = Math.max(result, r - l + 1);
        }
        
        return result;
    }
}
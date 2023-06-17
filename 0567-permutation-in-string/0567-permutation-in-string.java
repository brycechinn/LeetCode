class Solution {
    public boolean checkInclusion(String s1, String s2) {
        // approach: two arrays to store char counts
        
        if (s1.length() > s2.length()) {
            return false;
        }
        
        Map<Character, Integer> s1Map = new HashMap<>();
        Map<Character, Integer> s2Map = new HashMap<>();
        
        for (char c = 'a'; c <= 'z'; c++) {
            s1Map.put(c, 0);
            s2Map.put(c, 0);
        }
        
        for (int i = 0; i < s1.length(); i++) {
            char c1 = s1.charAt(i);
            char c2 = s2.charAt(i);
            
            s1Map.put(c1, s1Map.get(c1) + 1);
            s2Map.put(c2, s2Map.get(c2) + 1);
        }
        
        if (s1Map.equals(s2Map)) {
            return true;
        }
        
        int l = 0;
        int r = s1.length() - 1;
        
        while (r < s2.length()) {
            char lChar = s2.charAt(l);
            s2Map.put(lChar, s2Map.get(lChar) - 1);
            
            l++;
            r++;
            
            if (r < s2.length()) {
                char rChar = s2.charAt(r);
                s2Map.put(rChar, s2Map.get(rChar) + 1);
            }
            
            if (s1Map.equals(s2Map)) {
                return true;
            }
        }
        
        return false;
    }
}
class Solution {
    public boolean isAnagram(String s, String t) {
        // approach: two arrays to store char counts
        
        if (s.length() != t.length()) {
            return false;
        }
        
        s = s.toLowerCase();
        t = t.toLowerCase();
        
        int[] countsS = new int[26];
        int[] countsT = new int[26];
        
        for (int i = 0; i < s.length(); i++) {
            countsS[s.charAt(i) - 'a']++;
            countsT[t.charAt(i) - 'a']++;
        }
        
        for (int i = 0; i < 26; i++) {
            if (countsS[i] != countsT[i]) {
                return false;
            }
        }
        
        return true;
    }
}
class Solution {
    public boolean isAnagram(String s, String t) {
        // approach 1: sort strings then compare
        
        char sChars[] = s.toCharArray();
        char tChars[] = t.toCharArray();
        
        Arrays.sort(sChars);
        Arrays.sort(tChars);
        
        return Arrays.equals(sChars, tChars);
    }
}
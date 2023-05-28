class Solution {
    public boolean isAnagram(String s, String t) {
        // approach 1: sort strings then compare
        
        /*
        char sChars[] = s.toCharArray();
        char tChars[] = t.toCharArray();
        
        Arrays.sort(sChars);
        Arrays.sort(tChars);
        
        return Arrays.equals(sChars, tChars);
        */
        
        // approach 2: add chars to hashmap then compare
        
        Map<Character, Integer> sHash = new HashMap<>();
        Map<Character, Integer> tHash = new HashMap<>();
        
        for (char c : s.toCharArray()) {
            if (sHash.containsKey(c)) {
                sHash.put(c, sHash.get(c) + 1);
            } else {
                sHash.put(c, 1);
            }
        }
        
        for (char c : t.toCharArray()) {
            if (tHash.containsKey(c)) {
                tHash.put(c, tHash.get(c) + 1);
            } else {
                tHash.put(c, 1);
            }
        }
        
        return sHash.equals(tHash);
    }
}
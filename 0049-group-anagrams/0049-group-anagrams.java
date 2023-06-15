class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        // approach: hashmap of char count array : list of strings
        
        Map<String, List<String>> hashmap = new HashMap<>();
        
        for (String str : strs) {
            Integer[] buffer = new Integer[26];
            
            for (int i = 0; i < buffer.length; i++) {
                buffer[i] = 0;
            }
            
            for (int i = 0; i < str.length() ; i++) {
                // update key with char counts
                int index = str.charAt(i) - 'a';
                buffer[index]++;
            } 
            
            String key = new String(Arrays.toString(buffer));
            List<String> list = hashmap.computeIfAbsent(key, k -> new ArrayList<>());
            list.add(str);
        }
        
        return new ArrayList<>(hashmap.values());
    }
}
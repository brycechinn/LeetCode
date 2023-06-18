class TimeMap {
    // approach: hashmap of key : list of [val, timestamp]
    
    Map<String, List<Pair<String, Integer>>> hashmap;
    
    public TimeMap() {
        hashmap = new HashMap<>();
    }
    
    public void set(String key, String value, int timestamp) {
        if (!hashmap.containsKey(key)) {
            hashmap.put(key, new ArrayList<>());
        }
        
        hashmap.get(key).add(new Pair(value, timestamp));
    }
    
    public String get(String key, int timestamp) {
        if (!hashmap.containsKey(key)) {
            return "";
        }
        
        // binary search on timestamps
        List<Pair<String, Integer>> messages = hashmap.get(key);
        
        int l = 0;
        int r = messages.size() - 1;
        
        String result = "";

        while (l <= r) {
            
            int m = (l + r) / 2;
            
            int current = messages.get(m).getValue();
            
            if (current == timestamp) {
                return messages.get(m).getKey();
            }
            
            if (current > timestamp) {
                r = m - 1;
            } else {
                result = messages.get(m).getKey();
                l = m + 1;
            }   
        }
        
        return result;
    }
}

/**
 * Your TimeMap object will be instantiated and called as such:
 * TimeMap obj = new TimeMap();
 * obj.set(key,value,timestamp);
 * String param_2 = obj.get(key,timestamp);
 */
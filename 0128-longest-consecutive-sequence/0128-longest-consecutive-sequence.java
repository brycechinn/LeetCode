class Solution {
    public int longestConsecutive(int[] nums) {
        // approach: two pass array, one to find starts of sequences and one to
        // find longest sequence
        
        int result = 0;
        
        Set<Integer> hashset = new HashSet<>();
        List<Integer> starts = new ArrayList<>();
        
        for (int num : nums) {
            hashset.add(num);
        }
        
        for (int num : nums) {
            if (hashset.contains(num - 1)) {
                continue;
            }
            
            starts.add(num);
        }
        
        for (int start : starts) {
            int length = 1;
            int num = start;
            
            while (hashset.contains(num + 1)) {
                length++;
                num++;
            }
            
            result = Math.max(result, length);
        }
        
        return result;
    }
}
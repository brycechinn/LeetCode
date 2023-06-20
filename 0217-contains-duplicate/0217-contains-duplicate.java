class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> hashset = new HashSet<>();
        boolean result = false;
        
        for (int num : nums) {
            if (hashset.contains(num)) {
                return true;
            }
            
            hashset.add(num);
        }
        
        return result;
    }
}
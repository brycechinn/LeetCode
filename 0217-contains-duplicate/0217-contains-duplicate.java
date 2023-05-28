class Solution {
    public boolean containsDuplicate(int[] nums) {
        // approach: iterate through nums and add to set
        
        Set<Integer> set = new HashSet<>();
        
        for (int num : nums) {
            if (set.contains(num)) {
                return true;
            } else {
                set.add(num);
            }
        }
        
        return false;
    }
}
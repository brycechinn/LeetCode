class Solution {
    public int findDuplicate(int[] nums) {
        // approach: Floyd's Tortoise and Hare
        
        int slow = 0;
        int fast = 0;
        
        while (true) {
            slow = nums[slow]; // like slow.next
            fast = nums[nums[fast]]; // like fast.next.next
            
            if (slow == fast) {
                break;
            }
        }
        
        // now slow is at desired pos
        
        int slow2 = 0;
        
        while (true) {
            slow = nums[slow];
            slow2 = nums[slow2];
            
            if (slow == slow2) {
                return slow; // duplicate found
            }
        }
    }
}
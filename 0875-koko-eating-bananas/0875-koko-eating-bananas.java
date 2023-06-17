class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        // approach: binary search on piles.min, piles.max
        
        // get max of piles
        int max = 0;
    
        for (int pile : piles) {
            max = Math.max(max, pile);
        }
        
        // binary search on [1, max]
        int l = 1;
        int r = max;
        int k = max;
        int result = max;
        
        while (l <= r) {
            k = (l + r) / 2;
            int hours = 0;
            
            for (int pile : piles) {
                hours += Math.ceil((double) pile / k);
            }
            
            if (hours > h) {
                l = k + 1;
            } else {
                // potential new min
                result = Math.min(result, k);
                r = k - 1;
            }
        }
        
        return result;
    }
}
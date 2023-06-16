class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        // approach: hashmap of num : frequency then array of frequency : list of nums
        
        Map<Integer, Integer> hashmap = new HashMap<>();
        int[] result = new int[k];
        
        // hashmap of num : frequency
        for (int num : nums) {
            hashmap.put(num, hashmap.getOrDefault(num, 0) + 1);
        }
        
        /*
        for (Map.Entry<Integer, Integer> entry : hashmap.entrySet()) {
            System.out.println(entry.getKey() + " : " + entry.getValue());
        }
        */
        
        // array of frequency : list of nums
        List<Integer>[] freqs = new List[nums.length + 1];
        
        for (Map.Entry<Integer, Integer> entry : hashmap.entrySet()) {
            if (freqs[entry.getValue()] == null) {
                freqs[entry.getValue()] = new ArrayList<>();
            }
            
            freqs[entry.getValue()].add(entry.getKey());
        }
        
        /*
        for (List<Integer> list : freqs) {
            if (list == null) {
                continue;
            }
            
            for (Integer num : list) {
                System.out.print(num + " ");
            }
            System.out.println();
        }
        */
        
        int count = 0;
        for (int i = freqs.length - 1; i >= 0; i--) {
            if (freqs[i] == null) {
                continue;
            }
            
            for (int num : freqs[i]) {
                result[count] = num;
                count++;
                
                if (count >= k) {
                    return result;
                }
            }
        }
        
        return result;
    }
}
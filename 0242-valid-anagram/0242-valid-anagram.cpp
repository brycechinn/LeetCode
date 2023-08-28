class Solution {
public:
    bool isAnagram(string s, string t) {
        
        if (s.size() != t.size()) {
            return false;
        }
        
        array<int, 26> counts_s;
        array<int, 26> counts_t;
        counts_s.fill(0);
        counts_t.fill(0);
        
        for (int i = 0; i < s.size(); i++) {
            int index_s = static_cast<int>(s[i]) - static_cast<int>('a');
            int index_t = static_cast<int>(t[i]) - static_cast<int>('a');

            counts_s[index_s]++;
            counts_t[index_t]++;
        }
        
        return counts_s == counts_t;
    }
};
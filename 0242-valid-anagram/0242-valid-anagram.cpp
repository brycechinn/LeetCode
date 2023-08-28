class Solution {
public:
    bool isAnagram(string s, string t) {
        
        if (s.size() != t.size()) {
            return false;
        }
        
        vector<int> counts_s(26, 0);
        vector<int> counts_t(26, 0);
        
        for (int i = 0; i < s.size(); i++) {
            counts_s[s[i] - 'a']++;
            counts_t[t[i] - 'a']++;
        }
        
        return counts_s == counts_t;
    }
};
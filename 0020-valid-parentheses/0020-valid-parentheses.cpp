class Solution {
public:
    bool isValid(string s) {
        unordered_map<char, char> hashmap = {
            {'(', ')'},
            {'{', '}'},
            {'[', ']'}
        };
        
        stack<char> pars;
        
        for (char p : s) {
            if (hashmap.count(p)) {
                pars.push(p);
            } else {
                if (!pars.empty() && p == hashmap.at(pars.top())) {
                    pars.pop();
                } else {
                    return false;
                }                         
            }
        }
        
        return pars.empty();
    }
};
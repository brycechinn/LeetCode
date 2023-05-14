class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        # approach 1: scrub input then use left and right pointers, if at any
        # point the chars are different, return False
        
        '''
        def scrub(s):
            res = ''
            
            for char in s:
                if char.isalnum():
                    res += char.lower()   
                    
            return res
            
        string = scrub(s)
        
        l, r = 0, len(string) - 1
        
        while l < r:
            if string[l] != string[r]:
                return False
            
            l += 1
            r -= 1
            
        return True
        '''
        
        # approach 2: reduce space complexity by filtering chars as you go,
        # move pointers until they are at a valid char
        
        def alphaNum(c):
            return (ord('A') <= ord(c) <= ord('Z') or
                    ord('a') <= ord(c) <= ord('z') or
                    ord('0') <= ord(c) <= ord('9'))
        
        l, r = 0, len(s) - 1
        
        while l < r:
            while l < r and not alphaNum(s[l]):
                l += 1
            
            while r > l and not alphaNum(s[r]):
                r -= 1

            if s[l].lower() != s[r].lower():
                return False
            
            l += 1
            r -= 1
        
        return True
                
        
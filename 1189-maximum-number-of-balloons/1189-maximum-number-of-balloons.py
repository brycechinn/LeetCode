class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # approach: hashmap of char: count, then compare with target hashmap
        # time: O(n) space: O(n)
        
        target, target_map, text_map = 'balloon', defaultdict(int), defaultdict(int)
        
        for char in target:
            target_map[char] += 1
        
        for char in text:
            text_map[char] += 1
        
        res = len(text)
        for char, target_count in target_map.items():
            text_count = text_map[char]         
            res = min(res, text_count // target_count)
        
        return res
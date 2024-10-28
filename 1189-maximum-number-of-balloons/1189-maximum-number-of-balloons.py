class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # approach: hashmap of char: count, then compare with target hashmap
        # time: O(n) space: O(n)
        
        target, res = 'balloon', len(text)
        target_map, text_map= Counter(target), Counter(text)

        for char, target_count in target_map.items():
            text_count = text_map[char]         
            res = min(res, text_count // target_count)
        
        return res
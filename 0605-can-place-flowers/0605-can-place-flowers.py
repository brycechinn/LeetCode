class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        res, prev = 0, 0
        
        for i in range(len(flowerbed) - 1):
            next = flowerbed[i + 1]
            
            if prev == 0 and flowerbed[i] == 0 and next == 0:
                flowerbed[i] = 1
                res += 1
            
            prev = flowerbed[i]
        
        # check the last position
        if prev == 0 and flowerbed[-1] == 0:
            res += 1
        
        return res >= n
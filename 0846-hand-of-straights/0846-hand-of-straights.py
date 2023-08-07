class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        counts = collections.Counter(hand)
        hand.sort()

        for num in hand:
            if counts[num] == 0:
                continue
            
            counts[num] -= 1
            
            length = 1
            while length < groupSize:
                if num + length not in counts or counts[num + length] == 0:
                    return False
                
                counts[num + length] -= 1
                length += 1
            
        return True
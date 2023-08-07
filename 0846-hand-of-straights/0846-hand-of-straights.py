class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # approach: greedy, hashmap of num : count, sort nums, then
        # assemble groups one by one
        
        if len(hand) % groupSize != 0:
            return False
        
        counts = collections.Counter(hand)
        hand.sort()

        for num in hand:
            if counts[num] == 0:
                continue

            for i in range(num, num + groupSize):
                if i not in counts or counts[i] == 0:
                    return False
                
                counts[i] -= 1
            
        return True
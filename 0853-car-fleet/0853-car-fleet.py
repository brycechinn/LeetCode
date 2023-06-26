class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # approach:
        # 1. get arrival times of each car
        # 2. pair arrival times with start positions
        # 3. sort list of pairs by start position
        # 4. use stack to group car fleets

        length = len(position)
        arrivals = []
        pairs = []
        
        for i in range(length):
            # y = mx + b
            # x = (y - b) / m
            
            y, m, b = target, speed[i], position[i]
            x = (y - b) / m
            
            arrivals.append(x)
            pairs.append((position[i], arrivals[i]))

        pairs.sort(key=lambda x: x[0])

        stack = []
        for i in range(length - 1, -1, -1):
            arrival = pairs[i][1]
            
            if stack and arrival <= stack[-1]:
                continue
            
            stack.append(arrival)
        
        return len(stack)
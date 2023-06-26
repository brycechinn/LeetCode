class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # approach:
        # 1. get arrival times of each car
        # 2. pair arrival times with start positions
        # 3. sort list of pairs by start position
        # 4. use stack to group car fleets

        length = len(position)
        
        arrivals = [0] * length
        cars = [[] for _ in range(length)]
        
        for i in range(length):
            arrivals[i] = (target - position[i]) / speed[i]
            cars[i] = [position[i], arrivals[i]]

        cars.sort(key=lambda x: x[0])

        stack = []
        for i in range(len(cars) - 1, -1, -1):
            arrival = cars[i][1]
            
            if stack and arrival <= stack[-1]:
                continue
            
            stack.append(arrival)
        
        return len(stack)
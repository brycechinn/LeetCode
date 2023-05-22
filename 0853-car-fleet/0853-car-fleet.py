class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        
        # approach: create list of times that each car will reach the target,
        # e.g. times[i] is time that car with position[i] and speed[i] will
        # reach target. then maintain stack of times, "combining" times when
        # a slower time is in front of a faster time.
        
        times, cars, stack = [], [], []
        n = len(speed)
        
        for i in range(n):
            cars.append((speed[i], position[i]))
        
        cars.sort(key=lambda x: x[1])
        
        for i in range(n):
            y, m, b = target, cars[i][0], cars[i][1]
            x = (y - float(b)) / float(m)
            times.append(x)
            print(x)

        print(times)
            
        for time in times:
            while stack and time >= stack[-1]:
                stack.pop()
                
            stack.append(time)
        
        return len(stack)
            
            
        
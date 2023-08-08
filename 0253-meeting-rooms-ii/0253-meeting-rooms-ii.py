class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # approach: sort lists of starts an ends, then use two pointers to
        # increment and decrement number of rooms
        
        st = sorted([i[0] for i in intervals])
        en = sorted([i[1] for i in intervals])

        res, rooms = 0, 0
        i, j = 0, 0
        
        while i < len(st):
            if st[i] < en[j]:
                i += 1
                rooms += 1
            else:
                j += 1
                rooms -= 1
            
            res = max(res, rooms)
        
        return res
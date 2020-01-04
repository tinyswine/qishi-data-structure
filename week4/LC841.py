class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        checked_dict = {0 : 1}
        room_list = [0]
        
        i = 0
        
        while i < len(room_list):
            key = room_list[i]
            for j in rooms[key]:
                if not checked_dict.get(j, 0):
                    checked_dict[j] = 1
                    room_list.append(j)
            i += 1
                
        for i in range(len(rooms)):
            if not checked_dict.get(i, 0):
                return False
        return True
            
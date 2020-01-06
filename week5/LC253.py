"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def minMeetingRooms(self, intervals):
        # Write your code here
        
        result_list = []
        
        intervals_list = []

        for interval in sorted(intervals, key=lambda x: x.start):
            if result_list and result_list[0] < interval.start:
                heapq.heapreplace(result_list, interval.end)
            else:
                heapq.heappush(result_list, interval.end)
        
        return len(result_list)
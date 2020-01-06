class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        
        def calc_dist(p):
            return -(p[0] ** 2 + p[1] ** 2)
        
        result_list = []
        
        for p in points:
            if len(result_list) < K:
                heapq.heappush(result_list, (calc_dist(p), p))
            elif calc_dist(p) > result_list[0][0]:
                heapq.heapreplace(result_list, (calc_dist(p), p))
                
        return [i[1] for i in result_list]
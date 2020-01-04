class Solution(object):
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        
        times_dict = {}
        cost_dict = {}
        
        for i in range(1, N + 1):
            cost_dict[i] = float('inf')
        
        for i in times:
            u, v, w = i
            if times_dict.get(u, None):
                times_dict[u].append((w, v))
            else:
                times_dict[u] = [(w, v)]
            
        def dfs(u, cost):
            
            if cost_dict[u] <= cost:
                return
            
            cost_dict[u] = cost
            for w, v in sorted(times_dict.get(u, [])):
                dfs(v, cost + w)
                
        dfs(K, 0)
        
        for i in cost_dict.keys():
            if cost_dict[i] == float('inf'):
                return -1
        return max(cost_dict.values())
                
            
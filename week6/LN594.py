class Solution:
    """
    @param: source: A source string
    @param: target: A target string
    @return: An integer as index
    """
    def strStr2(self, source, target):
        # write your code here
        
        base = 256
        q = 101
        
        if (source == None) or (target == None):
            return -1
        
        n, m = len(source), len(target)
        h = 1
        
        if m > n:
            return -1
            
        if m == 0:
            return 0
        
        source_h = 0
        target_h = 0
        
        for i in range(m):
          if i > 0:
              h = (h * base) % q
          target_h = (ord(target[i]) + target_h * base) % q
          source_h = (ord(source[i]) + source_h * base) % q
          
        start = 0  
        
        while True:
           if (source_h == target_h) and (target == source[start : start + m]):
               return start
           start += 1
           if start + m > n:
               return -1
           source_h = ((source_h - ord(source[start - 1]) * h) * base  + ord(source[start + m - 1])) % q
           
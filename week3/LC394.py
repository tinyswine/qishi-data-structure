class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        tmp = ""
        s_num = []
        s_str = []
        cnt = 0
        for i in range(len(s)):
            if (s[i] >= '0' and s[i] <= '9'):
                cnt = 10 * cnt + int(s[i]) - 0
            elif (s[i] == '['):
                s_num.append(cnt)
                s_str.append(tmp)
                cnt = 0
                tmp = ""
            elif (s[i] == ']'):
                k = s_num[-1]
                s_num.pop()
                for j in range(k):
                    s_str[-1] += tmp
                tmp = s_str[-1]
                s_str.pop()
            else:
                tmp += s[i]
        if s_str:
            return s_str[-1]
        return tmp
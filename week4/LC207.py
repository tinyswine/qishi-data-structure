class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        
        pre_dict = {}
        taken_dict = {}
        
        for cur in range(numCourses):
            pre_dict[cur] = []
        
        for cur, pre in prerequisites:
            pre_dict[cur].append(pre)
        
        course_list = []
        for cur in pre_dict.keys():
            if not pre_dict[cur]:
                course_list.append(cur)
        
        while course_list:
            for pre in course_list:
                taken_dict[pre] = 1
                for cur in pre_dict.keys():
                    if pre in pre_dict[cur]:
                        pre_dict[cur].remove(pre)

            course_list = []
            for cur in pre_dict.keys():
                if (not pre_dict[cur]) and (not taken_dict.get(cur, 0)):
                    course_list.append(cur)
        
        if len(taken_dict) < numCourses:
            return False
        return True
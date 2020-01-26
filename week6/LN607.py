class TwoSum:
    """
    @param number: An integer
    @return: nothing
    """
    
    def __init__(self):
        self.num_list = []
    
    def add(self, number):
        # write your code here
        self.num_list.append(number)
    """
    @param value: An integer
    @return: Find if there exists any pair of numbers which sum is equal to the value.
    """
    def find(self, value):
        # write your code here
        cnt_dict = {}
        for number in self.num_list:
            if cnt_dict.get(number, 0):
                return True
            cnt_dict[value - number] = 1
        return False
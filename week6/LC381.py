from random import randint

class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.cnt_dict = {}
        self.num_list = []
        

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        self.num_list.append(val)
        
        if self.cnt_dict.get(val, 0):
            self.cnt_dict[val] += 1
            return True
        else:
            self.cnt_dict[val] = 1
            return False
        

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if self.cnt_dict.get(val, 0):
            self.cnt_dict[val] -= 1
            if not self.cnt_dict[val]:
                del self.cnt_dict[val]
                
            for i in range(len(self.num_list)):
                if self.num_list[i] == val:
                    break
            self.num_list = self.num_list[:i] + self.num_list[i + 1:]
            return True
        else:
            return False

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        i = randint(0, len(self.num_list) - 1)
        return self.num_list[i]


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
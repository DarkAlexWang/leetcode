class PhoneDirectory(object):

    def __init__(self, maxNumbers):
        """
        Initialize your data structure here
        @param maxNumbers - The maximum numbers that can be stored in the phone directory.
        :type maxNumbers: int
        """
        self.setused = set()
        self.num_list = [i for i in range(maxNumbers)]
        

    def get(self):
        """
        Provide a number which is not assigned to anyone.
        @return - Return an available number. Return -1 if none is available.
        :rtype: int
        """
        if len(self.num_list):
            num = self.num_list.pop()
            self.setused.add(num)
            return num
        else:
            return -1
        

    def check(self, number):
        """
        Check if a number is available or not.
        :type number: int
        :rtype: bool
        """
        return number not in self.setused
        

    def release(self, number):
        """
        Recycle or release a number.
        :type number: int
        :rtype: void
        """
        if number in self.setused:
            self.setused.remove(number)
            self.num_list.append(number)
        


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)

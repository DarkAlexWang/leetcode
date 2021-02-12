# @lc lang=python3
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.vals = []
        self.val_to_idx = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.val_to_idx:
            return False
        self.vals.append(val)
        self.val_to_idx[val] = len(self.vals) - 1
        return True


    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.val_to_idx:
            return False
        idx = self.val_to_idx[val]
        last_val = self.vals[-1]
        self.vals[idx] = last_val
        self.vals.pop()
        self.val_to_idx[last_val] = idx

        del self.val_to_idx[val]
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.vals)



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

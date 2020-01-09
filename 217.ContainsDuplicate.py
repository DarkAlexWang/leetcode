class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        distinct = {}
        for i in nums:
            if distinct.contains(i):
                return True
            else:
                distinct.add(i)
        return false

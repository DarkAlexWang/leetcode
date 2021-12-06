class Solution:
    def swapArray(self, array: list[int]) -> int:
        # move all 1 to front
        count1 = 0
        step = 0
        for num in array:
            if num == 0:
                step = step + 1
            else:
                count1 = count1 + step

        # move all 1 to end
        count2 = 0
        step = 0
        for num in array:
            if num == 1:
                step = step + 1
            else:
                count2 = count2 + step

        return min(count1, count2)

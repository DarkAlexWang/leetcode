class Solution:
    def reorder(self, arry, left, right):
        length = right - left + 1
        if length <= 2:
            return
        mid = (left + right)// 2
        lmid = left + (right - left + 1)// 4
        rmid = left + (right - left + 1) * 3 // 4
        self.reverse(arry, lmid, mid- 1)
        self.reverse(arry, mid, rmid - 1)
        self.reverse(arry, lmid, rmid - 1)

        self.reorder(arry, left, left + (lmid - left) * 2 -1)
        self.reorder(arry, left + (lmid - left) * 2, right)

    def reverse(arry, left, right):
        while left < right:
            tmp = arry[left]
            arry[left] = arry[right]
            arry[right] = tmp
            left += 1
            right -= 1

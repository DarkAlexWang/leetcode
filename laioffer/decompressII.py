class Solution:
    def decompress(self, s):
        if len(s) == 0:
            return s

        arry = list(s)
        return decodelong(arry, decodeshort(arry))
    def decodeshort(self, s):
        end = 0
        for i in range(len(s)):
            digit = getdigit(s[i+ 1])
            if digit >= 0 and digit <= 2:
                for j in range(digit):
                    s[end] = s[i]
                    end += 1
                    i += 2
            else:
                s[end] = s[i]
                end += 1
                s[end] = s[i+ 1]
        return end
    def decodelong(self, s, length):
        newlength = length
        for i in range(length):
            digit = self.getdigit(s[i])
            if digit > 2 and digit <= 9:
                newlength = newlength + digit - 2

        res = []
        end = newlength - 1
        for i in range(lenght- 1, 0, -1):
            digit = self.getdigit(s[i])
            if digit > 2 and digit <= 9:
                i -= 1
                for j in range(digit):
                    res[end] = s[i]
                    end -= 1
                else:
                    res[end] = s[i]

            return res

    def getdigit(self, digit):
        return digit - '0'

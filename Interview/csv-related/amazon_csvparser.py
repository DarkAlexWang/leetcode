#Given a string, convert it to a list of values separeted by coma. Called CSV parser.

#Example 1
#
#Input = ' "a","b","c" '
#
#Output = [a, b, c]
#// We are not adding the double quotes in the strings
#
#Example 2
#
#Input = "a","b,","c"
#
#Output = [a, "b," ,c]
#// If there is a comma in between the double quotes then it is part of the string and we add it into the result, so b will have the comma.
#
#Example 3
#
#Input = ' a,"b,",c '
#
#Output = [a,"b,",c]
#// We can also get the string without the double quotes around each value and use the comma to separate the values that doesn't have double
#quotes and add the inner commas in the values that have double quotes, for example the b have a comma in between the double quotes, but the a and c doesn't have double quotes around so we use the comma to separate them.
#
#We can assume that:
#
#    the string will fit in the memory.
#    if we have double quotes, we will get the same number of open double quotes as close double quotes

import collections
class Solution:
    def csvparser(self, s):
        #open_p, close_p, startwordat = 0, 0, 0
        #q = collections.deque()
        #path = ''
        #res = list()
        #foundchar = False
        #for i in range(len(s)):
        #    if s[i] == '"' and foundchar == False:
        #        open_p += 1
        #    elif s[i] == '"' and foundchar == True:
        #        close_p += 1
        #        while q:
        #            path += q.popleft()
        #            print(path)
        #        res.append(path)
        #    elif s[i] == ' ':
        #        continue
        #    elif s[i] != '"' and s[i] != ',':
        #        foundchar = True
        #        q.append(s[i])
        #    elif s[i] == ',':
        #        if close_p >= open_p:
        #            # add string we have seen so far and reset values
        #            res.append(s[startwordat:i])
        #            while q:
        #                q.popleft()
        #            startwordat = i + 1
        #            foundchar = False
        #            path = ''
        #            open_p, close_p = 0, 0

        #return res

        open_p, close_p, startwordat = 0, 0, 0
        res = []
        foundchar = False
        s += ','
        for i in range(len(s)):
            if s[i] == '"' and foundchar == False:
                open_p += 1
            elif s[i] == '"' and foundchar == True:
                close_p += 1
            elif s[i] == ' ':
                continue
            elif s[i] != '"' and s[i] != ',':
                foundchar = True
            elif s[i] == ',':
                if close_p >= open_p:
                    # add string we have seen so far and reset values
                    res.append(s[startwordat:i])
                    startwordat = i + 1
                    foundchar = False
                    open_p, close_p = 0, 0

        return res
if __name__ == "__main__":
    solution = Solution()
    input1 = 'a, "b,", c'
    input2 = '"a", "b", "c"'
    out1 = solution.csvparser(input1)
    out2 = solution.csvparser(input2)
    print('[%s]' % ','.join(map(str, out1)))
    print('[%s]' % ','.join(map(str, out2)))

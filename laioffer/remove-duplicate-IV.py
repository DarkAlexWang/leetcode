class Solution:
    def removeduplicateIV(self, string):
        ## using stack
        if len(string) <= 1:
            return
        i = 0
        stack = []
        while i < len(string):
            char = string[i]
            if len(stack) > 0 and string[i] == stack[-1]:
                while i < len(string) and char == string[i]:
                    i += 1
                stack.pop()
            else:
                stack.append(string[i])
                i += 1
        string = ""
        for j in range(len(stack)):
            string += stack[j]
        return string


        ## not using Stack
        #if string == '':
        #    return string
        #end = 0
        #array = list(string)
        #for i in range(1, len(array)):
        #    if end == -1 or array[i] != array[end]:
        #        array[end] = array[i]
        #        end += 1
        #    else:
        #        end -= 1
        #        while i + 1 < len(array) and array[i] == array[i -1]:
        #            i += 1
        #res = ''
        #for i in range(end + 1):
        #    res += array[i]
        #return res

if __name__ == '__main__':
    solution = Solution()
    res = solution.removeduplicateIV('abbbbbbac')
    print(res)

class Solution:
    def removespaces(self, string):
        if string is None:
            return string
        array = list(string)
        end = 0
        res = ''
        for i in range(len(array)):
            if array[i] == ' ' and (i == 0 or array[i - 1] == ' '):
                continue
            array[end] = array[i]
            end += 1
            #res += array[end]

        if end > 0 and array[end - 1] == ' ':
            return array[:end - 1]
        return "".join(array[:end])
if __name__ == '__main__':
    solution = Solution()
    ans = solution.removespaces(' for this  great evening!  c')
    print(ans)
#def normalizeString(s):
#  listStr = list(s) # Convert to string for modifying list
#  ind = 0
#  while ind < len(listStr) - 1:
#    if listStr[ind] == listStr[ind+1] and listStr[ind] == ' ':
#      listStr.pop(ind+1)
#    else:
#      ind += 1
#
#  # Check if first and last have spaces, if so remove them
#  if listStr[0] == ' ':
#    listStr.pop(0)
#  if listStr[-1] == ' ':
#    listStr.pop(-1)
#  return ''.join(listStr)

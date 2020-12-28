# "11+(4-2)*4"
# "11+4-2*4"
# + - * /
# 11 - 4 + 8 = 15
#
# stack 11 + 4 - 2 * 4
#  res = 11
# res = 11 + 4 = 15
# res = 15 - 2 = 13
# res = 13 * 4
# stack: [11, +, 4, -, 2 *]
# res = 4 * 2 = 8

# q = [ * 2 - 4 + 11]
# res = 4 * 2 = 8
# q = [8 - 4 + 11]

# Final res = 8 - 4  = 4
# q = [ 4 + 11]
# Final res = 4 + 11 = 15
import collections
class Solution:
    def calculate_str(self, input):
        q = collections.deque()
        path = ''
        n = len(input)
        final_res = []
        for i in range(n) :
            if input[i] not in ['+', '-', '*', '/']:
                path = path + input[i]

            elif input[i] not in ['*', '/']:
                digit = int(path)
                q.append(digit)
                q.append(input[i])
            else:
                digit = int(path)
                q.append(digit)
                q.append(input[i])
                j = i + 1
                while j < n and input[j] not in ['+', '-', '*', '/']:
                    right = input[j]
                    right_digit = int(right)
                    operator = q.popleft()
                    left_integer = q.popleft()
                    left_digit = int(left_integer)
                    if operator == '*':
                        res = left_integer * right_digit
                    else:
                         res = left_digit // right_digit
                    q.append(res)
        while q:
            left_integer = q.popleft()
            operator = q.popleft()
            right_integer = q.popleft()
            if operator == '+':
                final_res = left_integer + right_integer


            else:
                final_res = left_integer - right_integer
            q.append(final_res)
        return final_res

if __name__ == "__main__":
    solution = Solution()
    input = "11+4*2-3"
    res = solution.calculate_str(input)
    print(res)

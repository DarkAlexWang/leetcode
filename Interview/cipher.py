# zendesk interview
class Solution:
    def cipher(self, st):
        res = ''
        for char in st:
            if char.isalpha():
                num = ord(char) + 13
                if num > 122:
                    num = ord('a') + num - 123
                temp = chr(num)
                res += temp
            else:
                res += char
        print(res)
        return res

if __name__ == '__main__':
    solution = Solution()
    input = "hello world"
    solution.cipher(input)

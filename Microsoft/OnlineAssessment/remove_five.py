class Solution:
    def remove_five(self, num):
        if num > 0:
            str_num = str(num)
            for i, elem in enumerate(str_num):
                if i + 1 < len(str_num):
                    if elem == '5' and int(str_num[i])< int(str_num[i + 1]):
                        return int("".join(str_num[:i] + str_num[i+1:]))
                    else:
                        continue
                else:
                    if elem == '5':
                        return int("".join(str_num[:i]))
                    else:
                        return -1

        else:
            num *= -1
            str_num = str(num)
            for i, elem in enumerate(str_num):
                if i + 1 < len(str_num):
                    if elem == '5' and int(str_num[i]) > int(str_num[i + 1]):
                        return int("".join(str_num[:i] + str_num[i+1:])) * -1
                    else:
                        continue
                else:
                    if elem == '5':
                        return int("".join(str_num[:i])) * -1
                    else:
                        return -1

if __name__ == "__main__":
    solution = Solution()
    ans1 = solution.remove_five(15985)
    print(ans1)
    ans2 = solution.remove_five(-458125)
    print(ans2)
    ans3 = solution.remove_five(1534985)
    print(ans3)
    ans4 = solution.remove_five(-45248125)
    print(ans4)

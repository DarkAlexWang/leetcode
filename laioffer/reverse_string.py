class Solution:
    def reverse_string(self, string):
        if string is None or len(string) <= 1:
            return string
        st_list = list(string)
        left = 0
        right = len(st_list) - 1
        while left < right:
            st_list[left], st_list[right] = st_list[right], st_list[left]
            left += 1
            right -= 1
        return "".join(st_list)

if __name__ == "__main__":
    solution = Solution()
    ans = solution.reverse_string("abcdefg")
    print(ans)

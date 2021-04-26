import collections

class Solution:
    def items_in_containers(self, s, startIndices, endIndices):
        def floor_key(d, key):
            if key in d:
                return key
            return max(k for k in d if k < key)
        def ceil_key(d, key):
            if key in d:
                return key
            return min(k for k in d if k > key)
        dic = collections.defaultdict()
        n = len(startIndices)
        num_items = 0
        containerStart = -1
        for i in range(len(s)):
            if s[i] == '|':
                containerStart = i
                dic[i] = num_items
            elif containerStart >= 0:
                num_items += 1
        print(dic)
        result = []
        for i in range(n):
            left_key = ceil_key(dic, startIndices[i] - 1)
            print('left_key', left_key)
            right_key = floor_key(dic, endIndices[i] - 1)
            print('right_key', right_key)
            if left_key == None or right_key == None or left_key >= right_key:
                result.append(0)
            else:
                result.append(dic[right_key] - dic[left_key])
        return result
if __name__ == '__main__':
    solution = Solution()
    res = solution.items_in_containers('|**|*|*', [1, 1], [5, 6])
    print(res)

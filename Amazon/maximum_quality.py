import math
class Solution :
    def maximumQuality(self, packets, channels):
        packets.sort()
        res =0
        count= 0
        right=  len(packets) -1
        while count  <  channels -1 :
            res += packets[right]
            right-=1
            count +=1
        size = right +1

        if size % 2 ==1  :
            median  =  packets[size//2]
            res += median
        else :
            mid1 = size // 2
            mid2 = (size // 2 ) -1
            res += math.ceil((packets[mid1] + packets[mid2] )/2.0)
        return res
solution = Solution()
res = solution.maximumQuality([2,2,1,5,3] , 3 )
print(res)
res = solution.maximumQuality([2,2,1,5,3] , 2 )
print(res)
res = solution.maximumQuality([2,6,3] , 2 )
print(res)
res = solution.maximumQuality([1, 2, 3, 4, 5] , 2 )
print(res)
res = solution.maximumQuality([4, 3, 1, 2, 6, 5] , 3 )
print(res)

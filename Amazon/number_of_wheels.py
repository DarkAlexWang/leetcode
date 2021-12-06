class Solution:
    def findVehicles(self, vehicles):
        for i in range(len(vehicles)):
            if vehicles[i] % 2 != 0:
                vehicles[i] = 0
                continue
            numOfWays = vehicles[i] // 4 + 1
            vehicles[i] = numOfWays

        return vehicles

if __name__ == '__main__':
    solution = Solution()
    ans1 = solution.findVehicles([6, 3, 2])
    print(ans1)

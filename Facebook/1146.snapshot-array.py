#
# @lc app=leetcode id=1146 lang=python3
#
# [1146] Snapshot Array
#

# @lc code=start
from collections import defaultdict
class SnapshotArray:

    def __init__(self, length: int):
        self.dic = defaultdict(dict)
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        self.dic[self.snap_id][index] = val


    def snap(self) -> int:
        self.snap_id += 1
        self.dic[self.snap_id] = self.dic[self.snap_id - 1].copy()
        return self.snap_id - 1


    def get(self, index: int, snap_id: int) -> int:
        if index in self.dic[snap_id]:
            return self.dic[snap_id][index]
        else:
            return 0


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
# @lc code=end

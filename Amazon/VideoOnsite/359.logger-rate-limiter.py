#
# @lc app=leetcode id=359 lang=python3
#
# [359] Logger Rate Limiter
#

# @lc code=start
class Logger:

    def __init__(self):
        self.dict = collections.defaultdict()

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.dict:
            self.dict[message] = self.dict.get(message, timestamp) + 10
            return True
        elif self.dict[message] <= timestamp:
            self.dict[message] = timestamp + 10
            return True
        else:
            return False




# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
# @lc code=end

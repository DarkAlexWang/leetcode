class TransactionLogs:
    def process_logs(self, logs, threshold):
        dic = {}
        for logLine in logs:
            log = logLine.split(" ")
            dic[log[0]] = dic.get(log[0], 0) + 1
            if log[0] != log[1]:
                dic[log[1]] = dic.get(log[1], 0) + 1

        userIds = []
        for key, val in dic.items():
            if val >= threshold:
                userIds.append(key)
        userIds.sort()
        return userIds

if __name__ == "__main__":
    solution = TransactionLogs()
    ans1 = solution.process_logs(["345366 89921 45", "029323 38239 23", "38239 345366 15", \
            "029323 38239 77", "345366 38239 23", "029323 345366 13", "38239 38239 23"], 3)
    print(ans1)

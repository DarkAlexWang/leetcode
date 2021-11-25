while True:
    try:
        a = input()
        maxLen, maxStrs, curLen, curStr = 0, [], 0, ""
        for i, v in enumerate(a):
            if v.isnumeric():
                curLen += 1
                curStr += v
                if curLen > maxLen:
                    maxLen = curLen
                    maxStrs = [curStr]
                elif curLen == maxLen:
                    maxStrs.append(curStr)
            else:
                curLen = 0
                curStr = ""
        print("".join(maxStrs) + "," + str(maxLen))
    except:
        break

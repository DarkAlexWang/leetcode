class Solution:
    def reorderLogFiles(self, logs):
        text = []
        dig = []
        res = []
        for i in logs:
            l = []
            items = i.split(" ")
            if items[1].isdigit():
                dig.append(" ".join(items))
            else:
                text.append((items[0], ' '.join(items[1:])))

        text.sort(key=lambda x:(x[1], x[0]))

        res = [' '.join(tups) for tups in text]
        res.extend(dig)
        return res

if __name__ == "__main__":
    solution = Solution()
    logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
    res1 = solution.reorderLogFiles(logs)
    print(res1)

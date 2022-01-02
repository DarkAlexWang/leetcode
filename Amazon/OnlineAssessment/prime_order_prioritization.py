# lc = 937
class Solution:
    def reorder_log_files(self, logs):
        # split each log into two parts: <identifier, content>
        split1 = log1.split(" ", 2)
        split2 = log2.split(" ", 2)

        isDigit1 = split1[1][0].isdigit()
        isDigit2 = split2[1][0].isdigit()

        # case 1) both logs are letter-logs
        if not isDigit1 and not isDigit2:
            # first compare the content
            cmp = split1[1]

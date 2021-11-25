import sys

if __name__ == "__main__":
    for line in sys.stdin:
        strings = line.strip().split(' ')
        s, p = strings[0], strings[1]
        n = len(s)
        m = len(p)
        i, j = 0, 0
        min_to_delete = 0
        any_subseq_found = False

        if p is None:
            return False

from typing import List
from collections import deque

def fairIndexes(A: List[int], B: List[int]) -> int:
    # GET A PREFIX SUM OF EACH ARRAY
    for i in range(1, len(A)):
        A[i] += A[i - 1]
        B[i] += B[i - 1]

    # TRY EACH INDEX
    fair = 0
    for k in range(1, len(A)):
        left_A, right_A = A[k - 1], A[-1] - A[k - 1]
        left_B, right_B = B[k - 1], B[-1] - B[k - 1]
        fair += int(left_A == right_A == left_B == right_B)

    return fair
if __name__ == '__main__':
      #A = [int(x) for x in input().split()]
      #B = [int(y) for y in input().split()]
      A = [4, -1, 0, 3]
      B = [-2, 5, 0, 3]
      print(fairIndexes(A, B))

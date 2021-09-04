import sys
N, M = map(int, sys.stdin.readline().split())

for i in range(1, N*M+1, 1):
    if i%M == 0: print(i) 
    else: print(i, end=' ')


# 시간초과 두 번 걸리고 간신히 통과, 아래는 정답자들 중 하나의 코드
# n, m = map(int, input().split())
# for i in range(1, 1 + n*m, m):
#     print(' '.join(map(str, range(i, i+m))))
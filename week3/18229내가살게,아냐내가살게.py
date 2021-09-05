N, M, K = map(int, input().split())
total = 0
countNum = M
personNum = 0

for i in range(N):
    temp = []
    temp = input().split()
    total = 0
    for j in range(M):
        temp[j] = int(temp[j])
        total += temp[j]
        if total >= K:
            if countNum > j:
                countNum = j
                personNum = i
print(personNum+1, countNum+1)



# 백준 정답
# import sys
# n,m,k=map(int,input().split())
# a=[list(map(int,i.split()))for i in sys.stdin]
# h=[0]*n
# for i in range(m):
#     for j in range(n):
#         h[j]+=a[j][i]
#         if h[j]>=k:print(j+1,i+1);exit()

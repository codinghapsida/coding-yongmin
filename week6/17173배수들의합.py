N, M = map(int, input().split())
lst = list(map(int, input().split()))
sum = 0
for i in range(N+1):
    for j in lst:
        if j>i:
            break
        if i%j==0:
            sum+=i
            break
print(sum)
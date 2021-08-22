n = int(input())
num = [0 for _ in range(n)]
num = list(map(int, input().split()))
num.sort()
gap = []
total = 0
min_index = 0
k = num[n//2]

for i in range(n):
    gap.append(abs(num[i] - k))
    total += gap[i]


while k <= num[n-1]:
    k += 1
    temp = []
    min2 = 0
    for i in range(n):
        temp.append(abs(num[i] - k))
        min2 += temp[i]

    if min2 >= total:
        break
    else:
        total = min2
        min_index = k

k = num[n//2]
while k >= num[0]:
    k -= 1
    temp = []
    min2 = 0
    for i in range(n):
        temp.append(abs(num[i] - k))
        min2 += temp[i]

    if min2 > total:
        break
    else:
        total = min2
        min_index = k   
        
print(min_index)

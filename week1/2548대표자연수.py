n = int(input())
num = [0 for _ in range(n)]

num = list(map(int, input().split()))
total = sum(num)
average = total//n
gap = []

for i in range(n):
    gap.append(abs(num[i] - average))
min1 = sum(gap)

k = average
while k <= max(num):
    k += 1
    temp = []
    for i in range(n):
        temp.append(abs(num[i] - k))
    min2 = sum(temp)

    if min2 >= min1:
        break
    else:
        min1 = min2
        min_index = k

k = average
while k >= min(num):
    k -= 1
    temp = []
    for i in range(n):
        temp.append(abs(num[i] - k))
    min2 = sum(temp)

    if min2 > min1:
        break
    else:
        min1 = min2
        min_index = k

print(min_index)

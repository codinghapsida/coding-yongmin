N = int(input())
card = list(map(int, input().split()))
M = int(input())
num = list(map(int, input().split()))
card.sort()
count = {}
for i in card:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1

for i in num:
    if i in count:
        print(count[i], end=' ')
    else: print(0, end=' ')


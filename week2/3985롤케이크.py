length = int(input())
Number = int(input())
rollCake = [0 for _ in range(length+1)]

max1 = 0
max1_index = 0
max2 = 0
max2_index = 0

for i in range(Number):
    count = 0
    start, end = map(int, input().split())

    if (end-start) > max1: # 최대 기대 방청객
        max1 = end - start
        max1_index = i+1

    for j in range(start, end+1, 1):
        if rollCake[j] == 0:
            rollCake[j] = i+1
            count += 1  
    
    if count > max2: # 최대 실제 방청객
        max2 = count
        max2_index = i+1

print(max1_index)
print(max2_index)



N = int(input())

square = []


for i in range(N): square.append(list(map(int, input().split()))) 
min_l=(0-square[0][0])**2 + (0-square[0][1])**2
index_l=0
max_r=(0-square[0][2])**2 + (0-square[0][3])**2
index_r=0

for i in range(1, N, 1):
    temp1 = (0-square[i][0])**2 + (0-square[i][1])**2
    if min_l > temp1:
        min_l = temp1
        index_l = i
    temp2 = (0-square[i][2])**2 + (0-square[i][3])**2
    if max_r < temp2:
        max_r = temp2
        index_r = i

print((square[index_r][2]-square[index_l][0]) * (square[index_r][3] - square[index_l][1]))

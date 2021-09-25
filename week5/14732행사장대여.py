N = int(input())
square = []


for i in range(N): square.append(list(map(int, input().split()))) 
max = (square[0][2] - square[0][0])*(square[0][3] - square[0][1])
index_r=0
index_l=0

for i in range(1, N, 1):
    
    temp1=((square[i][2] - square[i][0])*(square[i][3] - square[i][1]))
    temp2=((square[index_r][2] - square[i][0])*(square[index_r][3] - square[i][1]))
    temp3=((square[i][2] - square[index_l][0])*(square[i][3] - square[index_l][1]))

    if temp1 > temp2:
        if temp1 > temp3:
            if max < temp1:
                max = temp1
                index_r = i
                index_l = i
        else:
            if max < temp3:
                max=temp3
                index_r = i
    else:
        if temp2>temp3:
            if max < temp2:
                max = temp2
                index_l=i
        else:
            if max < temp3:
                max = temp3
                index_r=i
    

print(max)

n = int(input())
count = []
for k in range(n):
    input()
    r, c = map(int, input().split())
    candy = []

    for i in range(r):
        str = input()
        candy.append(str)

    count.append(0)
    for i in range(r):
        for j in range(c):
            if candy[i][j] == chr(111):
                if (i-1) >= 0 and (i+1) <= (r-1):
                    if candy[i-1][j] == chr(118) and candy[i+1][j] == chr(94):
                        count[k] += 1
                if (j-1) >= 0 and (j+1) <= c-1:
                    if candy[i][j-1] == chr(62) and candy[i][j+1] == chr(60):
                        count[k] += 1

for k in range(n):
    print(count[k])

n = input()
n = int(n)
i = 0
ss = []
result = [[99]*(n+1) for i in range(n+1)]
str = ''

while i < 5*n:
    s = input()
    str += s
    i += 1

for i in range(0, n, 1):
    ss.append(str[i*35 : (i+1)*35])

for j in range(1, n+1, 1):
    for i in range(j+1, n+1, 1):
        count  = 0
        for k in range(0, 5*7, 1):
            if ss[j-1][k] != ss[i-1][k]:
                count += 1
        result[j][i] = count

min = 99
x = 0
y = 0
for j in range(1, n+1, 1):
    for i in range(j+1, n+1, 1):
        if min > result[j][i]:
            min = result[j][i]
            x = j
            y = i

print(x, y)

N, M = map(int, input().split())
ball = []
for i in range(M): ball.append(list(map(int, input().split())))
basket = []

for i in range(N): basket.append(0)
for i in range(M):
    for j in range(ball[i][0]-1, ball[i][1], 1):
        basket[j] = ball[i][2]

for i in basket:
    print(i, end=' ')
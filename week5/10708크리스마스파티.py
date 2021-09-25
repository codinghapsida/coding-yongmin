friendN = int(input())
gameN = int(input())
mafia = list(map(int, input().split()))
vote = []
count = []

for i in range(gameN):
    vote.append(list(map(int, input().split())))
for i in range(friendN+1):
    count.append(0)
for i in range(gameN):
    count[mafia[i]] += 1
    for j in range(friendN):
        if mafia[i]==j+1:
            continue
        if mafia[i] != vote[i][j]:
            count[mafia[i]] += 1
        else: count[j+1] += 1

for i in range(1, friendN+1, 1):
    print(count[i])
N = int(input())


for j in range(N):
    wordNum = int(input())
    word = [input() for _ in range(wordNum)]
    infoNum = int(input())
    print(f"Scenario #{j+1}:")
    for i in range(infoNum):
        pw = list(map(int, input().split()))
        for k in pw[1:]:
            print(word[k], end='')
        print()
    print()
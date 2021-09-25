for i in range(int(input())):
    A, B = map(int, input().split())
    sum = 0
    num=1
    i=0
    while i < (A/B):
        if num%2 != 0:
            sum += num
            i += 1
        num += 1
    print(sum)
        
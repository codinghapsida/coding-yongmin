money, package = map(int, input().split())

count = 0
while money>0:
    count += money
    money //= package

print(count)
N = input()

# 정수를 자릿수별로 분리하는 세 가지 방법
# 1
lst = []
for i in N:
    lst.append(int(i))

# 2
# N = int(N)
# while(N!=0):
#     lst.append(N%10)
#     N//10
#     #단 거꾸로 배열에 저장됨 (1의 자리부터 저장됨)

# 3 원소값을 모두 더하는 방법
# total = sum(map(int, N))

length = len(lst)
total1 = 0
total2 = 0

for i in range(0, length//2, 1):
    total1 += lst[i]
for i in range(length//2, length, 1):
    total2 += lst[i]

if total1==total2: print("LUCKY")
else: print("READY")


# 백준 정답 / 진짜 이렇게 풀어야된다;; 아직 파이썬 한참 멀었다;;

# n = input()
# d = len(n)//2
# print("LUCKY" if sum(map(int, n[:d])) == sum(map(int, n[d:])) else "READY")


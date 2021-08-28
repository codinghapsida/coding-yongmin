# 상근이는 체스판을 만들려고 한다.
# 체스판은 검정칸과 흰칸으로 이루어져 있다. 가장 왼쪽 위칸의 색은 검정색이고, 나머지 색은 검정과 흰색이 번갈아가면서 등장한다.
# 검정색은 'X'로, 흰색은 '.'로 표시한다.
# 상근이의 체스판은 R행 * C열로 이루어져 있어야 한다. 또, 각각의 행의 높이는 문자 A개만큼 이며, 각각의 열의 너비는 문자 B개 만큼이다.
# 예제 출력을 보고 이해하면 쉽다.
# R, C, A, B가 주어졌을 때, 상근이의 체스판을 출력하는 프로그램을 작성하시오.

# 첫째 줄에 두 양의 정수 R과 C가 주어진다. (1 ≤ R, C ≤ 10)
# 둘째 줄에 두 양의 정수 A와 B가 주어진다. (1 ≤ A, B ≤ 10)

# 출력은 R * A행 C * B열로 이루어져 있어야 하며, 문제에서 설명한 상근이의 체스판을 출력한다.


R, C = map(int, input().split())
A, B = map(int, input().split())

str1 = []
str2 = []

# X로 시작하는 줄 만들기
for i in range(C):
    if i%2==0:ch='X'
    else: ch='.'
    for j in range(B):
        str1.append(ch)

# .으로 시작하는 줄 만들기
for i in range(C):
    if i%2==0:ch='.'
    else: ch='X'
    for j in range(B):
        str2.append(ch)

#문자열 2개 리스트 하나로 합치기
str = []
str.append(str1)
str.append(str2)


for i in range(R):
    j = i%2
    for k in range(A):
        print("".join(str[j]))
        # ''.join()을 사용하면 리스트를 문자열로 변환할 수 있다.



# 백준 숏코딩 정답
# R, C = map(int, input().split())
# A, B = map(int, input().split())

# d = ['X', '.']

# for i in range(R*A):
#     for j in range(C*B):
#         print(d[(i//A + j//B)%2], end = '')
#     print()



## 여기서 처음 두 줄을 아래 세 줄과 대체 가능
## f = lambda:map(int, input().split())
## R, C = f()
## A, B = f()
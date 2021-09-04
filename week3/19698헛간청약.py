N, W, H, L = map(int, input().split())

W = W//L
H = H//L

if W*H <= N:
    print(W*H)
else: print(N)
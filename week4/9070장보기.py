import sys

T = int(sys.stdin.readline())
min_p = 0
min_ppg = 0

for i in range(T):
    N = int(sys.stdin.readline())
    for j in range(N):
        gram, price = map(float, sys.stdin.readline().split())
        ppg = price/gram

        if j==0: 
            min_ppg = ppg
            min_p = price

        else:
            if ppg < min_ppg:
                min_ppg = ppg
                min_p = price
            elif min_ppg == ppg:
                if price < min_p:
                    min_p = price
        
    print(int(min_p))

    

        

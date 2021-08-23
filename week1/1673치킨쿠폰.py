def miniCal(k, coupon):
    chicken = 0
    stamp = 0
    while 1:
        chicken += coupon
        stamp = coupon
        coupon = stamp//k
        if coupon == 0: break

    return chicken

def calculate():
    coupon = 0
    i = 0
    n = []
    k = []
    c = []

    while 1:
        try:
            str = input()

            n1, k1 = str.split()
            n1 = int(n1)
            k1 = int(k1)
            n.append(n1)
            k.append(k1)

            coupon = n[i]
            chicken = miniCal(k[i], coupon)
            c.append(chicken)
            i += 1
            
        except:
            return c
    


c = calculate()
for i in c:
    print(i)
def chillguy(n):
    r = bin(n)[2:]
    r = int(r, 30)
    r = bin(r)[2:][::-1]
    return int(r, 2)

for i in range(1, 1000):
    p=chillguy(i)
    if p > 10000000 and i%2==0:
        print(i)
        break

def f(n):
    n=str(n)
    r1=int(n[0])**2 + int(n[2])**2 + int(n[4])**2
    r2=int(n[1])**2 + int(n[3])**2 + int(n[5])**2
    r=r1*r2
    return r

def sch(n): #сумма чётных
    n=str(n)
    s=0
    for i in range(len(n)):
        if int(n[i])%2==0:
            s+=int(n[i])
    return s
            
def snch(n): #сумма нечётных
    n=str(n)
    s=0
    for i in range(len(n)):
        if int(n[i])%2!=0:
            s+=int(n[i])
    return s

for i in range(100000, 101000):
    r=f(i)
    if r >=1000:
        r -= snch(i)
    else:
        r+= sch(i)
    if r == 4233:
        print(i)
        break
        
        
    

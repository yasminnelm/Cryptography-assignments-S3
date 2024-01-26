
from cmath import sqrt
from math import gcd


n=3148240326296492491829836036538028522262397298543021512290073
for i in range(2,int(sqrt(n).real)):
    if (n%i==0):
        p1=n/i
        p2=i
        if (gcd(int(p1),int(i))==1):
            print("p1=",p1)
            print("p2=",i)
            break
        else:
            print("pas premiers")
if(p1*p2==n):
    print("p1=",p1)
    print("p2=",p2)
else:
    print("erreur")

import math

def moadele(a,b,c):
    delta = (b*b) - (4*a*c)
    if delta < 0:
        print("moadele javab haqiqi nadard.")
    elif delta == 0:
        a1 = -b / (2 * a)
        print("moadele 1 javab darad : " , a1)
    else:
        a1 = (-b - math.sqrt(delta)) / (2 * a)
        a2 = (-b + math.sqrt(delta)) / (2 * a)
        print("moadele 2 javab darad , javab haye  moadele : " , a1 , "," , a2)

a , b , c = input("enter a , b , c (for example : 3 , 4 , 1) : ").split(",",2)
a , b , c = int(a) , int(b) , int(c)

print("\n")

moadele(a,b,c)

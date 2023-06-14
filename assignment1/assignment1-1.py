
n1 , n2 , n3 = input("please enter the numbers : ").split(" ",2)

n1 , n2 , n3 = int(n1) , int(n2) , int(n3)

if n1 < n2+n3 and n2 < n1+n3 and n3 < n1+n2:
    print("is triangle!")
else:
    print("is not triangle!")

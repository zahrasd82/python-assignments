
name , g1 , g2 , g3 = input("please enter the name of the student and his/her grades : ").split(" ",3)

g1 , g2 , g3 = int(g1) , int(g2) , int(g3)

average =  (g1 + g2 + g3) / 3

if average >= 17:
    print(name  + " is Greate!")
elif average < 17 and average >= 12:
    print(name +  " is Normal!")
else:
    print(name + " is Fail!")

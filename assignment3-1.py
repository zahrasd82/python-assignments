import random

pc_number = random.randint(1,30)
n = 0
while True:
     user_number=int(input("enter number"))
     n += 1
     if user_number == pc_number: 
            print("well done,you won")
            break
     else:
          if user_number < pc_number:
                 print("go up") 
          else:
                   print("come down")



import random

shart = 1

print("are you ready!?")
while shart:
    num = random.randint(1,6)
    if num == 6:
        print("number 6 , again!")
        continue
    else:
        print("you rolled number" , num)
        shart = 0
        


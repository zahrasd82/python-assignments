import math


shart = 1


while shart:

    str = input("enter your operation : ").split()

    if len(str) == 3:
        n1 , op , n2 = str[0] , str[1] , str[2]
        n1 , n2 = int(n1) , int(n2)

        if op == "+":
            result = n1+n2 
        elif op == "-":
            result = n1-n2
        elif op == "/":
            result = n1/n2
        elif op == "*":
            result = n1*n2
    else:
        op , n1 = str[0] , str[1]
        n1 = int(n1)

        if op == "sin":
            result = math.sin(n1)
        elif op == "cos":
            result = math.cos(n1)
        elif op == "tan":
            result = math.tan(n1)
        elif op == "cot":
            result = math.cos(n1)/math.sin(n1)
        elif op == "factorial":
            result = math.factorial(n1)
        elif op == "radical":
            result = math.sqrt(n1)

    print("result : ",result)

    i = input("do you want to continue : ")
    if i == "NO":
        shart = 0
        continue
    

def fibonatchi(n):
    array = []
    a1 = 0
    a2 = 1
    for i in range(n):
        if i == 0:
            array.append(a2)
        else:
            array.append(a2 + a1)
            a1 = a2
            a2 = array[i]
    array = array[::-1]
    string = ""
    for i in range(n):
        if i == 0:
            string += str(array[i])
        else:
            string += " ,"+str(array[i])
    print(string)

        
n = int(input("enter n : "))
fibonatchi(n)

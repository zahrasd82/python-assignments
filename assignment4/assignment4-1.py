def draw_board(n,m):
    for row in range(n):
        str = ""
        for col in range(m):
            if row % 2 == 0:
                str += "#*"
            else:
                str += "*#"
        print(str)

n , m = input("enter n and m (for example : 8 , 45) : ").split(",",1)
n , m = int(n) , int(m)

print("\n")
draw_board(n,m)

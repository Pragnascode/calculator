def add (a,b):
    answer= a+b
    print(str(a) + "+" + str(b)+ "=" + str (answer) )
def sub (a,b) :
    answer = a - b
    print(str(a) + "-" + str(b)+"="+""+str(answer))
def mul (a,b):
    answer = a*b
    print(str(a) + "*" + str(b) +"=" +""+str(answer))
def div (a,b):
    answer = a/b
    print(str(a)+"/"+str(b)+"="+""+str(answer))
while True :
    print("a, addition")
    print("b,subtraction")
    print("c, multiplication")
    print("d, division")
    print("e , exit")
    choice = input("input your choice")
    if choice == "a" or choice == "A":
        print("addition")
        a= input("input first number")
        b= input("input second number")
        add(a,b)
    elif choice == "b" or choice == "B":
        print("subtraction")
        a = int(input("input first number"))
        b = int(input("input second number"))
        sub(a,b)
    elif choice == "c" or choice == "C" :
        print("multiplication")
        a = int(input("input first number"))
        b = int(input("input second number"))
        mul(a,b)
    elif choice == "d" or choice == "D" :
        print("division")
        a = int(input("input first number"))
        b = int(input("input second number"))
        div(a,b)
    elif choice == "exit":
        print("ending...")
        quit()



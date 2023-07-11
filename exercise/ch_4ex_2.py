def greatest_number(a,b,c):
    if (a>b and a>c):
        return a
    elif (b>a and b>c):
        return b
    else :
        return c

def big_number(a,b):
    if a>b:
        return a
    else :
        return b
num1 = int(input("enter a number 1 :  "))
num2 = int(input("enter a number 2 : "))
num3 = int(input("enter a number 3 : "))


def greatest_number(big_number,c):
    return big_number

print(f"{greatest_number(big_number(num1,num2),num3)} is bid number out of three ")
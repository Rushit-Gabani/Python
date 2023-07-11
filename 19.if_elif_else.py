age = int(input("enter your age : "))

if age==0 or age<0 :
    print("you can not watch ")
elif 1<age<=3:
    print("your ticket is : free ")
elif 3<age<=10:
    print("your ticket is :100")
elif 10<age<=60:
    print("your ticket is : 250")
else :
    print("your ticket is : 200")
    
    
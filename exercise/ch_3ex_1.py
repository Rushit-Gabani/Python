import random
a= random.randint(11,20)
print("random number between 11 and 20 is %s")
guess_number=int(input("enter your guess number : "))

if guess_number==a :
    print("you win !!!!!")
else :    
    if guess_number<a :
        print("to low actual number")
    else :        
        print("to high actual number")
import random
a= random.randint(11,20)
guess = 1
# print("random number between 11 and 20 is %s")
guess_number=int(input("enter your guess number between 11 and 20  : "))
game_over = False

while not game_over:
    if guess_number==a :
         print(f"you win !!!!!, you guess this number in {guess} time")
         game_over= True
    else :    
        if guess_number < a :
            print("to low actual number")
            
        else :        
            print("to high actual number")
        guess +=1                                        #dry keyword
        guess_number = int(input("guess again : "))              #use for 1 time write
        
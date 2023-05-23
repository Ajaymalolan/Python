#import random module
import random

#Welcome screen for the game
print("Welcome to the game, here are the rules:\n")
print("Rock wins against scissors \n paper wins against rock \n and scissors wins against paper.")
print("Your choices are Stone (s) Paper(p) Scissor (c) ")

#while loop with control
while True:
    control=input("1 to continue 0 to end ")
    if(control=="0"):
        break
   #generating random 
    auto_num=random.randint(0, 2)
    auto_cast="Scissor"
    if(auto_num==0):
        auto_cast="Stone"
    elif(auto_num==1):
        auto_cast="Paper"
    elif(auto_num==2):
        auto_cast=="Scissor"
        
    #getting user value
    cast=input("cast your choice \n stone.... \n paper.... \n scissor.... \n")
    if (cast=="s"):
        num=0
    elif(cast=="p"):
        num=1
    elif(cast=="c"):
        num=2
    else:
        print("Oops wrong")
        break
     
    #comparing values to get result
    if(auto_num==num):
        print("Computer casts ", auto_cast )
        print("Tie")
    elif(auto_num==0 and num==1):
        print("Computer casts " , auto_cast )
        print("You win!")
    elif(auto_num==1 and num==2):
        print("Computer casts " , auto_cast )
        print("You win!")
    elif(auto_num==2 and num==0):
        print("Computer casts " , auto_cast )
        print("You win!")
    elif(auto_num==1 and num==0):
        print("Computer casts " , auto_cast )
        print("You Lost")
    elif(auto_num==2 and num==1):
        print("Computer casts " , auto_cast )
        print("You Lost")
    elif(auto_num==0 and num==2):
        print("Computer casts " , auto_cast )
        print("You Lost")
    print("Thanks for playing!")  
    
    
    
    
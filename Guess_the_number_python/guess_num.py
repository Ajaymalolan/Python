import random
print("Welcome to guess the number game! \n")
key='Y'
while(key=='Y'):
    level=input("Enter difficulty level \n E - numbers less than 10 \n M - number less than 50 \n D - number less than 100 \n")
    if(level=='E'):
        x=10
    elif(level=='M'):
        x=50
    elif(level=='D'):
        x=100
    else:
        print("please use E, M and D (all caps) to choose difficulty level")
        continue
    gen=int(random.randint(1,x))
    print("Your number is generated!")
    num=int(input("Guess the number "))
    count=1
    while(gen!=num):
        count=count+1
        print("Wrong guess! But here is a clue")
        if(gen>num):
            print("Answer is higher")
        elif(gen<num):
            print("Answer is lesser")
        num=int(input("Don't give up now, Guess again!"))
    print("Finally you made it!")
    print("You only took",count,"guesses to finish")
    key=input("if you wish to continue playing the game enter Y (Caps) ")
print("Thanks for playing the game!")

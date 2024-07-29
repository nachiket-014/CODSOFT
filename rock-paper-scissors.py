# python programming internship in codsoft 
# task  -- rock-paper-scissors
import random

options = ['rock', 'paper', 'scissors']
computer = random.choice(options)    

while True:
    ask = int(input("press 1 to play and 2 to exit:"))
    if ask == 1 :
        print("options are ",options)
        user= input("Enter your Choice :- ").lower()  
        if user not in options :
            print ("INVALID INPUT")
        else:
            print("Computer Choice :-" + computer)
            if computer == user :
                print("It's a  tie")
            elif computer=="stone":
                if user=="paper":
                    print("User Wins !!")
                else:
                    print("computer Wins !!")
            elif computer=="paper":
                if user =="stone":
                    print ("User Wins !!")
                else :
                    print ("Computer Wins !!")
            elif computer=="scissors":
                if user =="stone":
                    print("User Wins !!")
                else:
                    print("Computer Wins !!")
    elif ask == 2:
        print("thank you for playing")
        break
    else:
        print("onvalid input")

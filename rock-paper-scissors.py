# python programming internship in codsoft 
# task  -- rock-paper-scissors

import random

options = ['rock', 'paper', 'scissors']



computerchoice = random.choice(options)

while True:

    ask = int(input("press 1 to play and 2 to exit:"))
    if ask == 1 :
        userschoice = input('Enter your choice (rock, paper or scissors): ')
        if userschoice == computerchoice:
            print("Your choice ",userschoice, "computer choice" ,computerchoice,"\n")
            print(" It's a tie!")
        elif userschoice == "rock":
            if computerchoice == "scissors":
                print("Your choice ",userschoice, "computer choice" ,computerchoice,"\n")
                print("You win! ")
            else:
                print("Your choice ",userschoice, "computer choice" ,computerchoice,"\n")
                print("You lose!")
        elif userschoice == "paper":
            if computerchoice == "rock":
                print("Your choice ",userschoice, "computer choice" ,computerchoice,"\n")
                print("You win! ")
            else:
                print("Your choice ",userschoice, "computer choice" ,computerchoice,"\n")
                print("You lose !")
        elif userschoice == "scissors":
            if computerchoice == "paper":
                print("Your choice ",userschoice, "computer choice" ,computerchoice,"\n")
                print("You win! ")
            else:
                print("Your choice ",userschoice, "computer choice" ,computerchoice,"\n")
                print("You lose !")
        else :
             print("invalid")
    elif ask == 2:
        print("thank you for playing")
        break
    else:
        print("onvalid input")

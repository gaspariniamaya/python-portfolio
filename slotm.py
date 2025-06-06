#Amaya Gasparini - Period 4 - 1/28/2024
#Slot Machine

#Init
symbols = ["🌟", "🌟", "💖", "💖", "⚡", "⚡", "🌙", "🌙", "7"]
credits = 100 #gives the player a system to spend or win credits
import random
import time
#Functions
#1.Introduction
#2.Ask player if they'd like to spin or quit
#3.Randomly pull three symbols from our list
#4.Display the three symbols
#5.Determine the outcome (Jackpot, Match, Loss) (IF ELIF ELSE)
def slot_machine():
    global credits
    while True:
        print("Welcome to the Slot Machine") #Introduces the game
        print("You have " + str(credits) + ". Each spin costs 10 credits")
        spin = input("Would you like to spin the slots? (S/Q)") #Asks player if they would like to spin or quit
        if spin == "S" and credits > 0:
            print("Spinning...") #Prints that it is spinning
            time.sleep(3) #Takes 3 seconds to reveal the spin outcomes, gives a cool effect
            credits = credits - 10
            slot1 = random.choice(symbols) #Randomizes the slot outcomes for each spin
            slot2 = random.choice(symbols)
            slot3 = random.choice(symbols)
            outcome = [str(slot1), str(slot2), str(slot3)]
            print("Current slots: " + str(outcome)) #Prints the random outcome the computer selected
            if outcome == ["7", "7", "7"]:
                print("JACKPOT!!!") #Determines what happens when player reaches jackpot
                credits = credits + 100
                print("Total Credits: " + str(credits))
            elif outcome == ["🌟", "🌟", "🌟"] or outcome == ["🌙", "🌙", "🌙"] or outcome == ["⚡", "⚡", "⚡"] or outcome == ["💖", "💖", "💖"]:
                print("WIN!") #Determines what happens when player reaches a win
                credits = credits + 50
                print("Total Credits: " + str(credits))
            else:
                print("Loss!") #Determines what happens when player doesn't get a jackpot or a win
                credits = credits + 0
                print("Total Credits: " + str(credits))
        elif spin == "S" and credits < 10: #doesn't let the player play if they don't have enough credits
            print("Sorry! You do not have enough credits.")
            break
        else:
            print("Thanks for playing") #if player decides to quit, the loop ends
            break

#Main
slot_machine() #codes the whole function

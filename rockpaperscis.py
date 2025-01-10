#Amaya Gasparini
#1/6/2025
#Rock Paper Scissors

#Init
import random
wins = 0
losses = 0
ties = 0
#functions
def rpc():
    while True:
        global wins
        global losses
        global ties
        print("Welcome to Rock Paper Scissors")
        print("Select rock, paper, or scissors")
        player = input("Selection: ")
        computer = random.randint(1,3)
        if computer == 1:
            computer = "rock"
            print("Computer chose rock")
        elif computer == 2:
            computer = "paper"
            print("Computer chose paper")
        elif computer == 3:
            computer = "scissors"
            print("Computer chose scissors")


        if player == "rock" and computer == "scissors":
            print("You have won")
            wins = wins + 1
            print("Computer wins: " + str(losses))
            print("Your wins: " + str(wins))
            print("Ties: " + str(ties))

        elif player == "rock" and computer == "paper":
            print("The computer has won")
            losses = losses + 1
            print("Computer wins: " + str(losses))
            print("Your wins: " + str(wins))
            print("Ties: " + str(ties))

        elif player == "paper" and computer == "rock":
            print("You have won")
            wins = wins + 1
            print("Computer wins: " + str(losses))
            print("Your wins: " + str(wins))
            print("Ties: " + str(ties))

        elif player == "paper" and computer == "scissors":
            print("The computer has won")
            losses = losses + 1
            print("Computer wins: " + str(losses))
            print("Your wins: " + str(wins))
            print("Ties: " + str(ties))

        elif player == "scissors" and computer == "rock":
            print("The computer has won")
            losses = losses + 1
            print("Computer wins: " + str(losses))
            print("Your wins: " + str(wins))
            print("Ties: " + str(ties))

        elif player == "scissors" and computer == "paper":
            print("You have won")
            wins = wins + 1
            print("Computer wins: " + str(losses))
            print("Your wins: " + str(wins))
            print("Ties: " + str(ties))

        elif player == "rock" and computer == "rock":
            print("Tie game")
            ties = ties + 1
            print("Computer wins: " + str(losses))
            print("Your wins: " + str(wins))
            print("Ties: " + str(ties))

        elif player == "paper" and computer == "paper":
            print("Tie game")
            ties = ties + 1
            print("Computer wins: " + str(losses))
            print("Your wins: " + str(wins))
            print("Ties: " + str(ties))

        elif player == "scissors" and computer == "scissors":
            print("Tie game")
            ties = ties + 1
            print("Computer wins: " + str(losses))
            print("Your wins: " + str(wins))
            print("Ties: " + str(ties))

        play = input("Would you like to play again? Yes or no: ")
        if play == "no":
            print("Thanks for playing")
            break

#main
rpc()

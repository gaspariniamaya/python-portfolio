#Pokemon Evolution
#Amaya Gasparini
#Init 
pokemon_level = 0 #the level of the pokemon starts at 0, will evolve
pokemon_name = "pichu" #initial name of the pokemon
day = 1 #how many days have been spent playing
wins = 0 #amount of wins
losses = 0 #amount of losses
import random 
#Functions
def train(): # Defines what happens when the pokemon trains
    print("Your pokemon did 10 pushups!")
    global pokemon_level
    pokemon_level = pokemon_level + 1 #levels up by 1 every training session
    print("You have leveled up to " + str(pokemon_level))

def gym_battle(): #pokemon battle
    global pokemon_level
    global wins
    global losses
    outcome = random.randint(1, 2) #winning or losing is random
    if outcome == 1:
        print("Good Job! You have won! Your pokemon has gained 2 levels")
        pokemon_level = pokemon_level + 2 #adds two levels
        wins = wins + 1 #adds a win to its record
    else:
        print("Oh no! You have lost. You have not evolved")
        losses = losses + 1 #adds a loss to its record

def rest(): #pokemon does not battle or train. also displays pokemon information
    print("Your pokemon's name is: " + str(pokemon_name))
    print("Your pokemon's level is: " + str(pokemon_level))
    print("Amount of wins: " + str(wins))
    print("Amount of losses: " + str(losses))
    
def quit(): #this ends the game
    print("Thanks for playing!")
    
def evolve(): 
    #Check to see if your pokemon is eligible to evolve
    #10 Change their name
    #20 Change name again
    global pokemon_name
    if pokemon_level >= 10:
        pokemon_name = "pikachu"
        print("Congrats! Your pokemon has evolved into pikachu")
    elif pokemon_level >= 20:
        pokemon_name = "raichu"
        print("Congrats! Your pokemon has evolved into raichu")
        
def final_boss(): #final battle of the game
    global pokemon_level
    global wins
    global losses
    outcome = random.randint(1, 2) 
    if pokemon_level >= 20: #can only do this if reached level 20 or higher
        print("You have made ito the final boss battle")
        if outcome == 1:
            print("Congrats! You have succeeded")
            wins = wins + 1
        else:
            print("You have lost, play again to have a successful conclusion")
            losses = losses + 1
    else:
        print("You are not eligible for the final boss. Level up first")
        

#Main 
while True: #introduces the game and its options
    print("Welcome to Pokemon Evolution")
    print("Chose an activity for Day: " +str(day))
    print("""1. Train
    2. Gym Battle
    3. Rest(Display Info)
    4. Final Boss Battle
    5. Quit""")
    activity = int(input("Activity for the day: "))
    if activity == 1:
        train()
        evolve()
        day = day + 1
    elif activity == 2:
        gym_battle()
        evolve()
        day = day + 1
    elif activity == 3:
        rest()
        day = day + 1
    elif activity == 4:
        final_boss()
        day = day + 1
    elif activity == 5:
        quit()

        
    


    
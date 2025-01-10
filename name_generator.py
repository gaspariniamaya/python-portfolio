#Amaya J Gasparini - Period 4
#Name Generator Project - What Animal Are You?

print("Welcome to Find Your Animal")
print("Answer the following questions to find out what animal matches you")
ans = input("Air (a) or Earth (e) ?")
if ans == "a":
    ans = input("Boat Ride (b) or Plan Ride (p) ?")
    if ans == "b":
        ans = input("Scales (s) or Fins (f) ?")
        if ans == "s":
            print("Your Animal is a Turtle!")
        else:
            print("Your Animal is a Dolphin!")
    if ans == "p":
        ans = input("Wisdom (w) or Beauty (b) ?")
        if ans == "w":
            print("Your Animal is a Parrot!")
        else:
            print("Your Animal is a Flamingo!")
if ans == "e":
    ans = input("Dependent (d) or Independent (i) ?")
    if ans == "d":
        ans = input("Going out (g) or Staying in (s) ?")
        if ans == "g":
            print("Your Animal is a Dog!")
        else:
            print("Your Animal is a Cat!")
    if ans == "i":
        ans = input("Strength (s) or Agility (a) ?")
        if ans == "s":
            print("Your Animal is a Lion!")
        else:
            print("Your Animal is a Cheetah!")
    
        
    
''' 
    Name: Snowball-Mania
    Author: 
    Date: 
    Class: AP Computer Science Principles
    Python: 
'''

import random

def main():
    # the main runner of the game
	  # welcome the player, gather names, and run the snowball fight!
    

    players = []
    print("Welcome to Snowball Mania!")
    name = input("What is your name? ")
    print("Great to have you here, " + name + "! Who do you want to play against?")
    opponent = input()
    print(name + " vs. " + opponent)
    nextplayer = ""

    players.append(name)
    players.append(opponent)

    difficulty = int(input("Choose a difficulty (any positive number): "))

    while nextplayer != "DONE":
        nextplayer = input("Are there any other opponents? If not, type DONE ")
        players.append(nextplayer)
    players.remove("DONE")
    
    choice = input("Do you want to play manual or auto mode? (M/A) ")

    if choice == "M" or choice == "m":
        choice = "manual"
    elif choice == "A" or choice == "a":
        choice = "auto"
    
    gameplay(name, players, choice, difficulty)

   

def gameplay(name, players, choice, difficulty):
    plrhitamt = []

    for player in players:
        plrhitamt.append(0)
    
    while len(players) > 1:
        thrower = random.choice(players)

        if choice == "manual" and thrower == name:
            print("\n\nYou have the snowball!\nWho do you want to throw the snowball at? (Use numbers)")

            for player in players:
                if player != name:
                    print("(" + str(players.index(player) + 1) + ") " + player)

            target = input()
            target = players[int(target) - 1]

        if choice == "auto" or thrower != name:
            target = random.choice(players)
        
        while (target == thrower):
            target = random.choice(players)
        print("\n" + thrower + " is throwing a snowball at " + target + "!")

        hitNum = random.randint(1,difficulty)
        success = hitResult(hitNum)

        if success == True:
            print("Its a hit! " + target + " was hit by " + thrower + ".")

            del plrhitamt[players.index(target)]
            players.remove(target)
            plrhitamt[players.index(thrower)] += 1
            
        else:
            print(thrower + " missed " + target + ".")
    if name == players[0]:
        print("\nYou won the game! You are really good!")
        print("\033[32mYou ended with: " + str(plrhitamt[0]) + " hits\033[0m")
    else:
        print("\n" + players[0] + " won the game! Congratulations!")
        print("\033[32m" + players[0] + " ended with: " + str(plrhitamt[0]) + " hits\033[0m")

def hitResult(hitNum):
    # based on the number that is passed in, return True or False 
    # indicating if this was a hit or a miss
    if hitNum == 1:
        return True

    return False

main()

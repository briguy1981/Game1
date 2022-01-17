import random

answer = input("Would you like to try a game? (yes/no)")
if answer.lower().strip() == "yes":
    print("Okay great, lets start")
    # print("lets start with finding out what you want to be.  Would you like to be? Press (1) for Farmer (2) for Fighter or (3) for Archer ")

    answer = input("Do you want to start in the street or room?")
    if answer.lower().strip() == "street":
        print("You look around and can't see much. The cityscape is in a complete blackout.")

    else:
        print("The room is dark, but there is some ambient light.")
        answer = input("Would you like to look around?")

        if answer.lower().strip() == "yes":
            print("You find a flashlight on the entryway table")

            answer = ("Do you want to go to the left or right?")
            if answer.lower().strip() == "left":
                print("To the left is a hallway with 2 doors.")
                answer = ("do you want to try door 1 or 2?")
                if answer.int("1"):
                    print("You enter a bathroom, there is nothing here")
                elif answer.int("2"):
                    print("you enter a office/den, Lets see what is in here.")
                else:
                    print("There is nothing in the hallway other than the doors, which one do you want to check?")
        else:
            print("It is dark inside, you run into the wall, and the game is over.")

else:
    print("That's to bad, maybe some other time then, .")


#####  Currently once getting past past flashlight it is not going to next line, exiting code
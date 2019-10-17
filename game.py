# This is our semester-long project:
# a text-based adventure game in the spirit of Zork, Adventure, etc.


def main():
    # Initialize some variables.
    score = 0
    #locations = ["bedroom", "hallway", "stairway", "street"]
    currentLocation = 0

    bedroom = "You are standing in a creepy old smelly " + \
        "bedroom filled with cockroaches crawling all over the bedsheets. You start to hear footsteps coming towards you."

    hallway = "You run into a hallway. The walls are filled claw marks all over them. Water is dripping from the ceiling" +\
        ". Someone whispers to you and tells you to get out."

    stairway = "You end up in a dark noisy staircase. Rats squeak and voices scream at you, making you scared and terrified. You tell yourself to find an exit but you are lost and don't know " + \
        "which stairway can lead to the exit. You see a little girl run down" + \
        " the stairway on your left and you decide to follow her."

    street = "You are standing in a street with nobody walking or no cars passing by. Only one light is on and it is flickering. The little girl you followed has led you outside. The little girl is waiting for you on the other side of the " + \
        "street. As you get closer, you reach out to her and check if she is okay. The little girl slowly opens her mouth and shows " + \
        "her sharp teeth and rips your arm off. You are never seen again."

    def scorePrint():
        """This function prints the score.

        Returns:
            Prints a message with the score.
        """
        print("Your score is", score)

    # "Main" code starts here
    print()
    print()
    # Welcome message
    print("██▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄██ ")
    print("Welcome to the Dark Zone")
    print("""Life is normal.  Or so you think.  
One day you are strolling along outside, enjoying the nice weather.  
Then your vision fades to black and you fall to the ground and pass out.  
When you wake up, you are somewhere else, somewhere you have never been before, with no memories of how you got there. 
You are in a dimly lit room.
You are terrified.""")

    print()
    print()

    # Print location and score
    print(bedroom)
    scorePrint()
    input("Press enter to continue")
    print()
    print()

    # Moves to next location and increases score.
    currentLocation += 1
    score += 5
    print(hallway)
    scorePrint()
    input("Press enter to continue")
    print()
    print()

    currentLocation += 1
    score += 5
    print(stairway)
    scorePrint()
    input("Press enter to continue")
    print()
    print()

    currentLocation += 1
    score += 5
    print(street)
    scorePrint()
    input("Press enter to continue")
    print()
    print()

    currentLocation += 1
    score += 5

    print()
    # Ending message
    print("Thanks for playing.")
    print("Copyright 2019.  Email the authors at " +
          "Colin.MacDonald1[at]marist.edu or Giovanni.Cordova1[at]marist.edu")


main()

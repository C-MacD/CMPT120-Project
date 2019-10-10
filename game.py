# This is our semester-long project:
# a text-based adventure game in the spirit of Zork, Adventure, etc.


def main():
    # Initialize some variables.
    score = 0
    #locations = ["bedroom", "hallway", "stairway", "street"]
    currentLocation = 0

    bedroom = "You are standing in a" + \
        "bedroom. You start to hear footsteps " + "coming towards you."

    hallway = "You run into a hallway" +\
        ". Someone whispers to you and tells you to get out."

    stairway = "You end up in a stairway" + ". You tell yourself to find an exit but you are lost and " + "don't know " + \
        "which stairway can lead to the exit. You see a little" + " girl run down" + \
        " the stairway on your left and you decide to follow her."

    street = "You are standing in a street" + ". The little girl you followed has led you outside. " + "The little girl is waiting for you on the other side of the " + \
        "street. As you get closer, you reach out to her and check if " + "she is okay. The little girl slowly opens her mouth and shows " + \
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
    print("Welcome to the Dark Zone")
    print("You wake up with no memories and the place is pitch black." +
          " You are terrified")

    # Print location and score
    print(bedroom)
    scorePrint()
    input("Press enter to continue")

    # Moves to next location and increases score.
    currentLocation += 1
    score += 5
    print(hallway)
    scorePrint()
    input("Press enter to continue")

    currentLocation += 1
    score += 5
    print(stairway)
    scorePrint()
    input("Press enter to continue")

    currentLocation += 1
    score += 5
    print(street)
    scorePrint()
    input("Press enter to continue")

    currentLocation += 1
    score += 5

    print()
    # Ending message
    print("Thanks for playing.")
    print("Copyright 2019.  Email the authors at " +
          "Colin.MacDonald1[at]marist.edu or Giovanni.Cordova1[at]marist.edu")


main()

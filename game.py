# This is our semester-long project:
# a text-based adventure game in the spirit of Zork, Adventure, etc.


def main():
    # Initialize some variables.
    score = 0
    # locations = ["bedroom", "hallway", "stairway", "street"]
    currentLocation = 0

    bedroom = ("You are standing in a creepy old smelly \n"
               "bedroom filled with cockroaches crawling all over the \n"
               "bedsheets. You start to hear footsteps coming towards you.")

    hallway = ("You run into a hallway. The walls are filled claw marks \n"
               "all over them. Water is dripping from the ceiling. \n"
               "Someone whispers to you and tells you to get out.")

    stairway = ("You end up in a dark noisy staircase. Rats squeak and \n"
                "voices scream at you, making you scared and terrified. \n"
                "You tell yourself to find an exit but you are lost and \n"
                "don't know which stairway can lead to the exit. \n"
                "You see a little girl run down the stairway on your left \n"
                "and you decide to follow her.")

    street = ("You are standing in a street with nobody walking or no \n"
              "cars passing by. Only one light is on and it is flickering. \n"
              "The little girl you followed has led you outside. \n"
              "The little girl is waiting for you on the other side of the \n"
              "street. As you get closer, you reach out to her and check \n"
              "if she is okay. The little girl slowly opens her mouth and \n"
              "shows her sharp teeth and rips your arm off. \n"
              "You are never seen again.")

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
    print("Life is normal.  Or so you think.  \n"
          "One day you are strolling along outside, enjoying the nice \n"
          "weather.  Then your vision fades to black and you fall to the \n"
          "ground and pass out.  When you wake up, you are somewhere else, \n"
          "somewhere you have never been before, with no memories of how \n"
          "you got there. You are in a dimly lit room. You are terrified.")

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

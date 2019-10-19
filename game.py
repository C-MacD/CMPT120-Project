# This is our semester-long project:
# a text-based adventure game in the spirit of Zork, Adventure, etc.


def main():
    # Initialize some variables.
    score = 0
    currentLocation = ""
    command = ""
    # Commands that can be used any time.
    generalCommands = ["quit", "help"]

    # Descriptions of all the locations.
    bedroom = ("You are standing in a creepy old smelly \n"
               "bedroom filled with cockroaches crawling all over the \n"
               "bedsheets. You start to hear footsteps coming towards you.")

    hallway = ("You run into a hallway. The walls are covered with claw \n"
               "marks . Water is dripping from the ceiling. \n"
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

    # This function does lots of stuff.
    # Parameters are the location you want and the current score.
    # It increases the score, prints the location, prints the score,
    # prints empty lines for formatting.
    # It returns the location and new score so you can update
    # the main variables.
    def handleLocation(location, score):
        score += 5
        print(location)
        print("Your score is", score)
        input("Press enter to continue")
        print()
        print()
        return location, score

    # Prints the welcome message
    def title():
        print()
        print()
        print("██▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄██ ")
        print("Welcome to the Dark Zone")
        print("Life is normal.  Or so you think.  \n"
              "One day you are strolling along outside, enjoying the nice \n"
              "weather.  Then your vision fades to black and you fall to \n"
              "the ground and pass out.  When you wake up, you are \n"
              "somewhere else, somewhere you have never been before, \n"
              "with no memories of how you got there. \n"
              "You are in a dimly lit room. You are terrified.")
        print()

    # Prints the copyright and email contact message.
    def ending():
        print("Thanks for playing.")
        print("Copyright 2019.  \n"
              "Email the authors at Colin.MacDonald1[at]marist.edu \n"
              "or Giovanni.Cordova1[at]marist.edu")

    # The parameters are lists of the general and special commands
    # based on the environment.
    # It asks the user to input a command.
    # If that command is in a list, it will process the command.
    # If it is a special command (in the validCommands list):
    # It takes the index of the command, prints the item after that index,
    # and checks for true/false in the item after that.
    # The format of a valid command is:
    # [command, what gets printed, True if it breaks out of the loop]
    def processCommand(generalCommands, validCommands):
        # Ask for a command
        command = input("Enter a command: ").lower()
        # The loop
        while True:
            if command == "quit":
                break
            elif command == "help":
                print(generalCommands)
                # Prints every third item, the commands
                for i in range(0, len(validCommands), 3):
                    print(validCommands[i])
                command = input("Enter a command: ").lower()

            elif command in validCommands:
                # Finds the item right after the command, the description,
                # and prints it
                index = validCommands.index(command)+1
                print(validCommands[index])
                # If the item after that is true, break the loop
                if(validCommands[index+1]):
                    break
                command = ""
            # Bug checker
            elif (command in generalCommands or command in validCommands):
                print("You just found a bug!")
                print("This is a valid command but was not coded in.")
                command = ""
            # Gets a new command if you put in something invalid.
            else:
                command = str(
                    input(
                        "Enter a valid command.  Enter 'help' for a list: "
                    )).lower()

    # ----------------------------------------------------------
    # ----------------------------------------------------------

    # "Main" code starts here

    title()

    currentLocation, score = handleLocation(bedroom, score)

    # [command, what gets printed, True if it breaks out of the loop]
    validCommands = [
        "open door", "You open the door and enter the next room.", True,
        "jump", "You jump.", False]
    processCommand(generalCommands, validCommands)

    currentLocation, score = handleLocation(hallway, score)

    currentLocation, score = handleLocation(stairway, score)

    currentLocation, score = handleLocation(street, score)

    print()
    # Ending message

    ending()


main()

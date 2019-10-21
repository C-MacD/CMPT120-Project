# This is our semester-long project:
# a text-based adventure game in the spirit of Zork, Adventure, etc.


def main():
    # Commands that can be used any time.
    generalCommands = ["quit", "help"]

    # The format of a valid command is:
    # [command, what gets printed, True if it breaks out of the loop,
    #   the new location]
    # TODO: The last two fields could be merged.

    # Descriptions of all the locations.
    # TODO: These all need work.
    bedroom = ("You are standing in a creepy old smelly \n"
               "bedroom filled with cockroaches crawling all over the \n"
               "bedsheets. You start to hear footsteps coming towards you.")
    bedroomCommands = [
        "open door", "You open the door and enter the next room.",
        True, "hallway",

        "jump", "You jump.", False, None]

    hallway = ("You run into a hallway. The walls are covered with claw \n"
               "marks. Water is dripping from the ceiling. \n"
               "Someone whispers to you and tells you to get out.")
    hallwayCommands = [
        "open door", "You open the door and enter the next room.",
        True, "stairway"]

    stairway = ("You end up in a dark noisy staircase. Rats squeak and \n"
                "voices scream at you, making you scared and terrified. \n"
                "You tell yourself to find an exit but you are lost and \n"
                "don't know which stairway can lead to the exit. \n"
                "You see a little girl run down the stairway on your left \n"
                "and you decide to follow her.")
    stairwayCommands = [
        "open door", "You open the door and enter the next room.",
        True, "street"]

    street = ("You are standing in a street with nobody walking or no \n"
              "cars passing by. Only one light is on and it is flickering. \n"
              "The little girl you followed has led you outside. \n"
              "The little girl is waiting for you on the other side of the \n"
              "street. As you get closer, you reach out to her and check \n"
              "if she is okay. The little girl slowly opens her mouth and \n"
              "shows her sharp teeth and rips your arm off. \n"
              "You are never seen again.")
    streetCommands = [
        "continue", "Well, you made it.", True, "win"]

    win = "Congratulations!  You win!!"
    winCommands = []

    # The big lists.
    # List of strings.
    locations = ["bedroom", "hallway", "stairway", "street", "win"]
    # List of variables
    locationDescriptions = [bedroom, hallway, stairway, street, win]
    # List of lists
    locationCommands = [bedroomCommands, hallwayCommands,
                        stairwayCommands, streetCommands, winCommands]

    # Prints the welcome message
    def title():
        print("\n\n██▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄██ \n")
        print("Welcome to the Dark Zone")
        print("Life is normal.  Or so you think.  \n"
              "One day you are strolling along outside, enjoying the nice \n"
              "weather.  Then your vision fades to black and you fall to \n"
              "the ground and pass out.  When you wake up, you are \n"
              "somewhere else, somewhere you have never been before, \n"
              "with no memories of how you got there. \n"
              "You are in a dimly lit room. You are terrified.")

    # Prints the copyright and email contact message.
    def ending():
        print("\nThanks for playing. \n")
        print("Copyright 2019.  \n"
              "Email the authors at Colin.MacDonald1[at]marist.edu \n"
              "or Giovanni.Cordova1[at]marist.edu")
        print()
        print("██▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄██ ")

    # The parameters are a list of the general commands,
    # a list of the locations (strings),
    # a list of the descriptions of the locations
    # (variables pointing to strings),
    # and the locationCommands - a list of lists.
    #
    # It asks the user to input a command.
    # If that command is in a list, it will process the command.
    # If it is a special command (in the validCommands list):
    # It takes the index of the command, prints the item after that index,
    # and checks for true/false in the item after that,
    # and then sets the location to whatever is specified.
    # The format of a valid command is:
    # [command, what gets printed, True if it breaks out of the loop,
    #   the new location]

    def processCommand(generalCommands, locations, locationDescriptions,
                       locationCommands):
        # Some initial stuff specific to this loop
        score = 0
        locationIndex = 0
        playGame = True
        validCommand = False

        while playGame:
            # Should fire once every time entering a new location
            currentLocation = locations[locationIndex]
            validCommands = locationCommands[locationIndex]
            print()
            print()
            print(locationDescriptions[locationIndex])
            score += 5
            print("Your score is", score)

            if currentLocation == "win":
                playGame = False
                validCommand = True

            while not validCommand:
                # Ask for a command until it is deemed valid enough.
                command = input("Enter a command: ").lower()

                # Will quit out of both while loops
                if command == "quit":
                    playGame = False
                    validCommand = True

                # Prints out all possible commands for the location.
                elif command == "help":
                    print("▼--------▼")
                    print("Here are all the commands you can use")
                    print(generalCommands)
                    # Prints every fourth item, the commands
                    for i in range(0, len(validCommands), 4):
                        print(validCommands[i])
                    print("▲--------▲")

                elif command in validCommands:
                    # Finds the index of the command.
                    i = validCommands.index(command)
                    print()
                    # Prints the description (the index after the command)
                    print(validCommands[i+1])
                    # If the item after that is true, break the loop
                    if(validCommands[i+2]):
                        validCommand = True
                        # Sets the new location index to be the same as
                        # the new location.
                        locationIndex = locations.index(validCommands[i+3])
                    command = ""

                # Bug checker
                elif (command in generalCommands or command in validCommands):
                    print("You just found a bug!")
                    print("This is a valid command but was not coded in.")
                    print("It should be impossible to get here.")
                    command = ""

                # Tells you if you put in something invalid.
                else:
                    print("Enter a valid command.  Enter 'help' for a list.")

            validCommand = False

    # ----------------------------------------------------------
    # ----------------------------------------------------------

    # "Main" code starts here

    title()

    processCommand(generalCommands, locations,
                   locationDescriptions, locationCommands)

    ending()


main()

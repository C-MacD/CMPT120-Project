from player import player
from location import location
from item import itemClass


def main():

    def title():
        """Prints the welcome message
        """

        print("\n\n██▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄██ \n")
        print("Welcome to the Dark Zone")
        print("Life is normal.  Or so you think.  \n"
              "One day you are strolling along outside, enjoying the nice \n"
              "weather.  Then your vision fades to black and you fall to \n"
              "the ground and pass out.  When you wake up, you are \n"
              "somewhere else, somewhere you have never been before, \n"
              "with no memories of how you got there. \n"
              "You are in a dimly lit room. You are terrified. \n")

    title()

    # ----------------------------------------------------------
    # ----------------------------------------------------------

    player1 = player()
    player1.setName(input("What is your name? "))
    print("Hi " + player1.getName()+". Welcome to The Dark Zone.\n")

    # ----------------------------------------------------------
    # ----------------------------------------------------------

    flashlight = itemClass(
        "Flashlight", "You grab the flashlight, and turn it on.\n"
        "Now you can see where you are going.", False, True)

    bedroom = location("bedroom")
    hallway = location("hallway")
    stairway = location("stairway")
    street = location("street")
    bathroom = location("bathroom")
    # 6
    # 7
    # 8

    bedroom.setDescription(
        "You are standing in a creepy old smelly \n"
        "bedroom filled with cockroaches crawling all over the \n"
        "bedsheets. You start to hear footsteps coming towards you.\n"
        "There is a flashlight on the ground next to you")

    bedroom.addCommands(
        {"1. Open door": hallway,
         "2. Equip flashlight": flashlight,
         "3. Jump": "You jump."
         })

    pointlessList = [bedroom.description, hallway.description,
                     stairway.description, street.description,
                     bathroom.description]
    # ----------------------------------------------------------
    # ----------------------------------------------------------

    def goto(location):
        if(not player1.hasVisited(location)):
            player1.increaseScore(5)
        player1.setLocation(location)

    # ----------------------------------------------------------
    # ----------------------------------------------------------
    # ----------------------------------------------------------
    # ----------------------------------------------------------

    goto(bedroom)
    validCommands = ["inventory", "help", "quit", "points", "map"]

    def gameLoop():
        currentLocation = player1.getLocation()
        # Print location description if it is a new place.
        if(player1.inNewLocation()):
            print(currentLocation.getDescription())
        # TODO: Print special case descriptions.

        print("\nWhat would you like to do?")
        locationCommands = currentLocation.getCommands()
        for item in locationCommands:
            # Prints possible commands that will work in the location
            print(item)
        # Get command
        command = input("Enter a command: ")
        print()
        # Check for being valid
        valid = False
        while(not valid):
            try:
                if(type(int(command)) == int):
                    for item in locationCommands:
                        if(str(command)in item):
                            valid = True
                            key = item
                            value = locationCommands[item]
            except ValueError:
                pass
            try:
                if(command.lower() in validCommands):
                    command = command.lower()
                    valid = True
            except AttributeError:
                pass
            if(not valid):
                print("Sorry, that is an invalid command.  \n"
                      "You can enter 'help' for a list.")
                command = input("Enter a command: ")
                print()

        # TODO: open inventory
        if(command == "inventory"):
            print()
            # Print inventory
            # Get input

        elif(command == "quit"):
            # Quits
            return False

        elif(command == "help"):
            # Prints help
            print(validCommands)
            # for item in locationCommands:
            # print(item)

        elif(command == "points"):
            # Prints points
            print("You have "+player1.getPoints()+" points!")

        # TODO: Print map
        elif(command == "map"):
            print()
            # Print map

        # If it is a room
        elif(type(value) == location):
            # Go to that room
            goto(value)

        # If it is an item:
        elif(type(value) == itemClass):
            print()
            # If it shouldn't appear in inventory
            if(not value.shouldAppearInInventory()):
                # Print message
                print(value.getMessage())
            else:
                # Add to inventory
                player1.addItem(item)
            # Remove the command either way
            locationCommands.pop(key)

        return True

    playGame = True
    while(playGame):
        playGame = gameLoop()

    # ----------------------------------------------------------
    # ----------------------------------------------------------
    # ----------------------------------------------------------
    # ----------------------------------------------------------

    def ending():
        """Prints the copyright and email contact message.
        """
        print("\nThanks for playing. \n")
        print("Copyright 2019.  \n"
              "Email the author at Colin.MacDonald1[at]marist.edu")
        print()
        print("██▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄██ ")

    ending()


main()

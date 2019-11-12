from player import player
from location import location


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
    print("Hi " + player1.getName()+". Welcome to The Dark Zone.")

    # ----------------------------------------------------------
    # ----------------------------------------------------------

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
         "2. Equip flashlight": "You grab the flashlight, and turn it on.\n"
         "Now you can see where you are going.",
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
        # Print location description
        print(currentLocation.getDescription())
        # Print possible commands (also inventory, help, quit)
        # print(validCommands)
        print("\nWhat would you like to do?")
        locationCommands = currentLocation.getCommands()
        for item in locationCommands:
            print(item)
        # Get command
        command = input("Enter a command: ")
        # Check for being valid
        valid = False
        while(not valid):
            try:
                if(type(int(command)) == int):
                    for item in locationCommands:
                        if(str(command)in item):
                            valid = True
                            value = locationCommands[item]
            except:
                pass
            try:
                if(command.lower() in validCommands):
                    command = command.lower()
                    valid = True
            except:
                pass
            if(valid == False):
                print(
                    "Sorry, that is an invalid command.  You can enter 'help' for a list.")
                command = input("Enter a command: ")

        # If open inventory:
        if(command == "inventory"):
            print()
            # Print inventory
            # Get input
        # If quit:
        elif(command == "quit"):
            print()
            return False
            # Quit
        # If help:
        elif(command == "help"):
            print(validCommands)
            # Print help
        # If points
        elif(command == "points"):
            print("You have "+player1.getPoints()+" points!")
            # Print points
        # If map
        elif(command == "map"):
            print()
            # Print map

        # If it is a room
        elif(type(value) == location):
            goto(value)

            # run goto function
        # If it is an item:
        elif(type(value) == item):
            print()
            # If it doesn't appear in inventory
                # Print message
            # Else
                # Add to inventory
            # Remove the command

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

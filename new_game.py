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
    knife = itemClass(
        "Knife", "You grab the knife.  You feel slightly safer", True, False)

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
        "There is a flashlight on the ground next to you"
    )
    bedroom.addCommands({
        "1. Open door": hallway,
        "2. Equip flashlight": flashlight,
        "3. Jump": "You jump."
    })

    hallway.setDescription(
        "You run into a hallway. The walls are covered with claw \n"
        "marks. Water is dripping from the ceiling. \n"
        "Someone whispers to you and tells you to get out.\n"
        "You see a knife in a corner"
    )
    hallway.addCommands({
        "1. Equip knife": knife,
        "2. Open door": stairway,
        "3. Go back": bedroom
    })

    stairway.setDescription(
        "You end up in a dark noisy staircase. Rats squeak and \n"
        "voices scream at you, making you scared and terrified. \n"
        "You tell yourself to find an exit but you are lost and \n"
        "don't know which stairway can lead to the exit. \n"
        "You see a little girl run down the stairway on your left."
    )
    stairway.addCommands({
        "1. go left": street,
        "2. go right": bathroom,
        "3. go back": hallway
    })

    street.setDescription(
        "You are standing in a street with nobody walking or no \n"
        "cars passing by. Only one light is on and it is flickering. \n"
        "The little girl you followed has led you outside. \n"
        "The little girl is waiting for you on the other side of the \n"
        "street. As you get closer, you reach out to her and check \n"
        "if she is okay. The little girl slowly opens her mouth and \n"
        "shows her sharp teeth and rips your arm off. \n"
        "You are never seen again."
    )
    street.addCommands({})  # TODO: Win game

    bathroom.setDescription(
        "All the doors upstairs are locked, except for a bathroom.\n"
        "The door is propped open with a doorstop so you go in.\n"
        "It appears to be empty."
        "On the other side of the bathroom you see another,"
        "which leads into the livingroom"
    )
    bathroom.addCommands({
        "1. Search room": "You find absolutely nothing of interest except \n"
        "for the fact that someone seems to have stolen all the toilet paper.",
        "2. Go back": stairway
    })

    pointlessList = [bedroom.getDescription(), hallway.getDescription(),
                     stairway.getDescription(), street.getDescription(),
                     bathroom.getDescription()]
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

        # TODO: use inventory
        # Don't forget this is not a requirement.
        if(command == "inventory"):
            print("Here is what you have:")
            print(player1.getInventory())
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

        # If it is a descriptive string
        elif(type(value) == str):
            print(value)

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
                player1.addItem(value)
            # Remove the command either way
            locationCommands.pop(key)

        # A “time limit” by counting number of moves and checking for some max
        player1.increaseMoves(1)
        if(player1.getMoves() > player1.MAX_MOVES):
            pass
        return True

    # ------------------------

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

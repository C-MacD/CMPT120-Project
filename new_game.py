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

    # TODO: Win game
    bedroom = location("bedroom")
    hallway = location("hallway")
    stairway = location("stairway")
    street = location("street")
    bathroom = location("bathroom")
    closet = location("closet")
    shop = location("shop")
    office = location("office")

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
        "2. Go forwards": stairway,
        "3. Go right": closet,
        "4. Go back": bedroom
    })

    stairway.setDescription(
        "You end up in a dark noisy staircase. Rats squeak and \n"
        "voices scream at you, making you scared and terrified. \n"
        "You tell yourself to find an exit but you are lost and \n"
        "don't know which stairway can lead to the exit."
    )
    stairway.addCommands({
        "1. Go left, down the stairs": street,
        "2. Go right, up the stairs": bathroom,
        "3. Go back": hallway
    })

    street.setDescription(
        "You are standing in a street with nobody walking and no \n"
        "cars passing by. Only one light is on and it is flickering. \n"
        "The road is littered with debris, making it potentially impossible\n"
        "to cross.  A few feet down the sidewalk you are standing on,\n"
        "there is an open door."
    )
    street.addCommands({
        "1. Try to cross street":
            "The debris prove to be too hard to navigate\n"
            "and you can't find a way across.",
        "2. Go in the open door": shop,
        "3. Go back": stairway
    })

    bathroom.setDescription(
        "All the doors upstairs are locked, except for a bathroom.\n"
        "The door is propped open with a doorstop so you go in.\n"
        "It appears to be empty."
    )
    bathroom.addCommands({
        "1. Search room": "You find absolutely nothing of interest except \n"
        "for the fact that someone seems to have stolen all the toilet paper.",
        "2. Go back": stairway
    })

    closet.setDescription(
        "You are now in a small closet.  There is only one item: a jacket.\n"
        "It looks like it could fit you."
    )
    closet.addCommands({
        "1. Equip jacket": "You put on the jacket and start feeling warmer.",
        "2. Leave room": hallway
    })

    shop.setDescription(
        "You are in a looted grocery store.  All the shelves that you can\n"
        "see are empty.  You spot another door in the back."
    )
    shop.addCommands({
        "1. Search store":
            "You wander around.  All the shelves are indeed empty.\n"
            "The door in the back looks like it leads to an office.",
        "2. Open door": office,
        "3. Go back": street
    })

    office.setDescription(
        "The door opens up into a small room.  It is the store's office.\n"
        "You see a safe with the door open and contents missing.\n"
        "Other than that, the rest of the office is strangely untouched.\n"
        "There is a small cot in one corner of the room."
    )
    office.addCommands({
        "1. Sleep": "Congrats! You made it to the end.\n"
                    "Enter 'points' to see your score and 'quit' to exit."
    })

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
        else:
            print("[You are in the " + currentLocation.getName()+"]")
        # TODO: Print special case descriptions.

        print("\nWhat would you like to do?")
        locationCommands = currentLocation.getCommands()
        for item in locationCommands:
            # Prints possible commands that will work in the location
            # If they can go to a location that they have been to before,
            # print the name of the location.
            if(type(locationCommands[item]) == location
               and player1.hasVisited(locationCommands[item])):
                print(str(item)+" (" + locationCommands[item].getName()+")")
            else:
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
            locationCommands.pop(key)

        # If it is a room
        elif(type(value) == location):
            # Go to that room
            goto(value)

        # If it is an item:
        elif(type(value) == itemClass):
            print()
            # If it shouldn't appear in inventory
            if(not value.shouldAppearInInventory()):
                pass
            else:
                # Add to inventory
                player1.addItem(value)
            # Remove the command either way
            print(value.getMessage())
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

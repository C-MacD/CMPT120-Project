from player import Player
from location import Location
from item import Item


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

    # Player setup.
    player1 = Player()
    player1.setName(input("What is your name? "))
    print("Hi " + player1.getName()+". Welcome to The Dark Zone.\n")

    # ----------------------------------------------------------
    # ----------------------------------------------------------

    # Create items.
    flashlight = Item(
        "Flashlight", -1, "You grab the flashlight, and turn it on.\n"
        "Now you can see where you are going.",
        "The flashlight lights up the room")
    knife = Item(
        "Knife", -1, "You grab the knife.  You feel slightly safer",
        "You swing the knife.")
    waterBottle = Item(
        "Water bottle", 1, "You grab the water bottle.",
        "You drink the water and feel refreshed.")
    jacket = Item("Warm jacket", -1,
                  "You put on the jacket and start feeling warmer.",
                  "The jacket is warm.")

    # Create rooms.
    bedroom = Location("bedroom")
    hallway = Location("hallway")
    stairway = Location("stairway")
    street = Location("street")
    bathroom = Location("bathroom")
    closet = Location("closet")
    shop = Location("shop")
    office = Location("office")

    # Add items to rooms.
    bedroom.addItem(flashlight)
    hallway.addItem(knife)
    shop.addItem(waterBottle)
    closet.addItem(jacket)

    # Add descriptions and commands to rooms.
    bedroom.setDescription(
        "You are standing in a creepy old smelly \n"
        "bedroom filled with cockroaches crawling all over the \n"
        "bedsheets. You start to hear footsteps coming towards you."
    )
    bedroom.addCommands({
        "1. Open door": hallway,
        "2. Take flashlight": flashlight,
        "3. Jump": "You jump."
    })

    hallway.setDescription(
        "You run into a hallway. The walls are covered with claw \n"
        "marks. Water is dripping from the ceiling. \n"
        "Someone whispers to you and tells you to get out."
    )
    hallway.addCommands({
        "1. Take knife": knife,
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
        "1. Examine room": "You find absolutely nothing of interest except \n"
        "for the fact that someone seems to have stolen all the toilet paper.",
        "2. Go back": stairway
    })

    closet.setDescription(
        "You are now in a small closet.  Only one thing is hung up."
    )
    closet.addCommands({
        "1. Take jacket": jacket,
        "2. Leave room": hallway
    })

    shop.setDescription(
        "You are in a looted grocery store.  All the shelves that you can\n"
        "see are empty.  You spot another door in the back.\n"
        "You wander around.  All the shelves are indeed empty.\n"
        "The door in the back looks like it leads to an office."
    )
    shop.addCommands({
        "1. Open door": office,
        "2. Go back": street,
        "3. Take water bottle": waterBottle
    })

    office.setDescription(
        "The door opens up into a small room.  It is the store's office.\n"
        "You see a safe with the door open and contents missing.\n"
        "Other than that, the rest of the office is strangely untouched.\n"
        "There is a small cot in one corner of the room."
    )
    office.addCommands({
        "1. Sleep in the cot": ""
    })

    # ----------------------------------------------------------
    # ----------------------------------------------------------

    # Move player to a location and increase score if needed.
    def goto(location):
        if(not player1.hasVisited(location)):
            player1.increaseScore(5)
        player1.setLocation(location)

    # ----------------------------------------------------------
    # ----------------------------------------------------------
    # ----------------------------------------------------------
    # ----------------------------------------------------------

    # Initial location.
    goto(bedroom)
    # General commands that will work anywhere.
    validCommands = ["search", "s", "inventory", "i", "use",
                     "look around", "help", "quit", "points", "map"]

    # The main game loop.
    def gameLoop():

        # ---------- Show information to player
        currentLocation = player1.getLocation()
        # Print location description if it is a new place.
        if(player1.inNewLocation()):
            print(currentLocation.getDescription())
        else:
            print("[You are in the " + currentLocation.getName()+"]")

        print("\nWhat would you like to do, "+player1.getName()+"?")
        locationCommands = currentLocation.getCommands()
        for item in locationCommands:
            # Prints possible commands that will work in the location
            # If they can go to a location that they have been to before,
            # print the name of the location.
            if(type(locationCommands[item]) == Location
               and player1.hasVisited(locationCommands[item])):
                print(str(item)+" (" + locationCommands[item].getName()+")")
            # Prints items that can be picked up only if room is searched.
            elif(currentLocation.getSearched()
                 or not type(locationCommands[item]) == Item):
                print(item)

        # -------------- Get command
        command = input("Enter a command: ")
        print()
        # Check for being valid
        valid = False
        while(not valid):
            try:
                if(type(int(command)) == int):
                    for item in locationCommands:
                        if(str(command)in item):
                            if(currentLocation.getSearched()
                               or not type(locationCommands[item]) == Item):
                                # Checks for being intiger.
                                # Checks for being a room.
                                # Checks for room searched if item.
                                valid = True
                                key = item
                                value = locationCommands[item]
            except ValueError:
                pass

            try:
                if(command.lower() in validCommands):
                    # If it is a standard command.
                    command = command.lower()
                    valid = True
            except AttributeError:
                pass

            if(not valid):
                # Invalid commands.
                print("Sorry, that is an invalid command.  \n"
                      "You can enter 'help' for a list.")
                command = input("Enter a command: ")
                print()

        # ---------------Responces to standard commands

        # Player can use stuff in their inventory.
        if(command == "inventory" or command == "i" or command == "use"):
            # First print what is available.
            print(player1.getName()+", here is what you have:")
            i = 1
            print("0. (Exit inventory)")
            for item in player1.getInventory():
                print(str(i) + ".", item)
                i += 1

            # Get input until valid
            cmd = input("What item do you want to use? ")
            while(not cmd.isdigit()):
                print("Please enter an integer.  Enter 0 to exit inventory.")
                cmd = input("What item do you want to use? ")
            cmd = int(cmd)

            # Check if number refers to something.
            if(cmd == 0 or cmd > len(player1.getInventory())):
                pass
            else:
                # If an item is selected, use it.
                index = cmd-1
                selectedItem = player1.inventory[index]
                selectedItem.useItem()
                if(selectedItem.getUses() == 0):
                    player1.inventory.remove(selectedItem)

        # Search the room.
        elif(command == "search" or command == "s"):
            currentLocation.search()
            print("You search the room.")
            if(len(currentLocation.items) == 0):
                print("You didn't find any new items.")
            else:
                # Fancy print formatting for finding multiple things.
                print("You found ", end="")
                i = 1
                for item in currentLocation.getItems():
                    if(len(currentLocation.getItems()) == 1):
                        print("a", item.getName())
                    elif(i == len(currentLocation.getItems())):
                        print("and a", item.getName()+".")
                    else:
                        print("a", item.getName()+", ", end="")
                    i += 1
                print()

        elif(command == "quit"):
            # Quits
            return "Kill"

        elif(command == "help"):
            # Prints help
            print(validCommands)

        elif(command == "points"):
            # Prints points
            print(player1.getName()+", you have " +
                  player1.getPoints()+" points!")

        elif(command == "look around"):
            # Prints the room's long description.
            print(currentLocation.getDescription())

        # Prints a simple map
        elif(command == "map"):
            print("""
         Office
            |
          Shop
            |
         Street - Stairs - Bathroom
                     |
                  Hallway - Closet
                     |
                  Bedroom
                  """)

        # If it is a descriptive string (only a string and not an object)
        elif(type(value) == str):
            # Print the description and remove it from the list.
            print(value)
            locationCommands.pop(key)

        # If it is a room
        elif(type(value) == Location):
            # Go to that room
            goto(value)

        # If it is an item:
        elif(type(value) == Item):
            print()
            # If it shouldn't appear in inventory
            if(value.getUses() == 0):
                pass
            else:
                # Add to inventory, remove from location.
                player1.addItem(value)
                currentLocation.removeItem(value)
            # Print pickup message, remove from command list.
            print(value.getPickupMessage())
            locationCommands.pop(key)

        # A “time limit” by counting number of moves and checking for some max
        # Currently does nothing.
        player1.increaseMoves(1)
        if(player1.getMoves() > player1.MAX_MOVES):
            pass

        # If in the office, run the win/loose scenario.
        # Must bring knife to office to win, otherwise you loose.
        if(currentLocation == office):
            # Setting the scene.
            print("Suddenly, a zombie jumps out at you from behind the\n"
                  "office's desk.\n"
                  "It stumbles towards you, arms reaching for you.\n"
                  "You have no time to turn around and open the door\n"
                  "behind you, because the zombie would attack your back.\n"
                  "Your only choice is to attack the zombie.")
            if("Knife" in player1.getInventory()):
                # Brought knife, win
                print("1. Stab the zombie with your knife.")
                input("(Press enter to use the knife)")
                print()
                print("You stab the zombie in the head and leave the knife\n"
                      "in its head.  The zombie reaches for you, but you\n"
                      "avoid it.  The zombie takes half a step forwards\n"
                      "and freezes in place.\n"
                      "It collapses onto the ground and stops moving.")
                print("------------------")
                print("Congratulations!  Your knife has saved you.\n"
                      "You have won the game!!!")
                print()
                input("Press enter to continue")
                return "Win"
            else:
                # No knife, loose.
                print("1. Punch the zombie.")
                input("(Press enter to punch)")
                print()
                print("You give the zombie a solid punch, but it manages to\n"
                      "grab your hand and bite your arm.\n"
                      "You have been infected.\n"
                      "You collapse to the ground and your vision\n"
                      "fades to black.\n"
                      "Your last thought is you wondering what would have\n"
                      "happened if you had a weapon to defend yourself with.")
                print("------------------")
                print("You loose.")
                print()
                input("Press enter to continue")
                return "Loose"
        else:
            # Continue normal playing if in any other room.
            return "True"

    # ------------------------

    # The game loop (getting commands and stuff)
    playGame = "True"
    while(playGame == "True"):
        playGame = gameLoop()

        if(playGame == "Kill"):
            # If quit is entered.
            return False

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
        print("------------------")
        print()

    ending()

    # Ask to play again.
    playAgain = input("Want to play again? Yes or no: ")
    if("y" in str(playAgain).lower()):
        return True
    else:
        return False


# Will play the game forever until false is returned.
go = True
while (go):
    go = main()

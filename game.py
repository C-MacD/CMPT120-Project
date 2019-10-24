# This is our semester-long project:
# a text-based adventure game in the spirit of Zork, Adventure, etc.


def main():
    # Commands that can be used any time.
    generalCommands = ["quit", "help"]

    # The format of a valid command is:
    # [command, what gets printed, the new location]

    # Descriptions of all the locations.
    # TODO: These all need work.
    bedroom = ("You are standing in a creepy old smelly \n"
               "bedroom filled with cockroaches crawling all over the \n"
               "bedsheets. You start to hear footsteps coming towards you.\n"
               "There is a flashlight on the ground next to you")
    bedroomCommands = [
        "equip flashlight", "You grab the flashlight, and turn it on.\n"
        "Now you can see where you are going.", None,

        "open door", "You open the door and enter the next room.",
        "hallway",

        "jump", "You jump.", None]

    hallway = ("You run into a hallway. The walls are covered with claw \n"
               "marks. Water is dripping from the ceiling. \n"
               "Someone whispers to you and tells you to get out.\n"
               "You see a knife in a corner")
    hallwayCommands = [
        "equip knife", "You grab the knife.  You feel slightly safer",
        None,

        "open door", "You open the door and enter the next room.",
        "stairway",

        "go back", "You turn around and walk back into the bedroom",
        "bedroom"]

    stairway = ("You end up in a dark noisy staircase. Rats squeak and \n"
                "voices scream at you, making you scared and terrified. \n"
                "You tell yourself to find an exit but you are lost and \n"
                "don't know which stairway can lead to the exit. \n"
                "You see a little girl run down the stairway on your left.")
    stairwayCommands = [
        "go left", "You follow the girl.  \n"
        "Luckily for you, it seems that this is the exit.", "street",

        "go right", "You climb the stairs", "bathroom",

        "go back", "You turn around and walk back into the hallway",
        "hallway"]

    bathroom = ("All the doors upstairs are locked, except for a bathroom.\n"
                "The door is propped open with a doorstop so you go in.\n"
                "It appears to be empty." 
                "On the other side of the bathroom you see another," 
                "which leads into the livingroom")
    bathroomCommands = [
        "search room", "You find absolutely nothing of interest except for\n"
        "the fact that someone seems to have stolen all the toilet paper.",
        None,

        "go forward", "You open the door amd start to move into the a different room",
        "livingroom"]

    livingroom = ("As you leave the bathroom, you see a livingroom.\n"
              "All lights are turned off except for a small nightlight"
              "and your flashlight batteries have died.\n"
              "Once you step into the livingroom, you feel an evil presence near you.\n"
              "The wind started to blow really hard that it sounded like someone is banging against the window.\n"
              "As you try to flick the switch for the lights, you can't \n" 
              "see where you are steping and trip on the leg of a table." )
    livingroomCommands = [
        "look around", "You heard banging on the windows so you take\n"
        "out you knife but then you realize that it just the wind blowing hard"
        , None, 
        
        "find light switch", "You find the light switch but you trip on\n" 
        "the leg of the table" , None, 
        
        "go back", "You turn around and walk back to the stairs", 
        "stairway"]
              

    street = ("You are standing in a street with nobody walking or no \n"
              "cars passing by. Only one light is on and it is flickering. \n"
              "The little girl you followed has led you outside. \n"
              "The little girl is waiting for you on the other side of the \n"
              "street. As you get closer, you reach out to her and check \n"
              "if she is okay. The little girl slowly opens her mouth and \n"
              "shows her sharp teeth and rips your arm off. \n"
              "You are never seen again.")
    streetCommands = [
        "continue", "Well, you made it.", "win",

        "go back", "You turn around and walk back up the stairs",
        "stairway"]

    win = "Congratulations!  You win!!"
    winCommands = []

    # The big lists.
    # List of strings.
    locations = ["bedroom", "hallway", "stairway", "street", "win",
                 "bathroom"]
    # List of variables
    locationDescriptions = [bedroom, hallway, stairway, street, win, bathroom]
    # List of lists
    locationCommands = [bedroomCommands, hallwayCommands, stairwayCommands,
                        streetCommands, winCommands, bathroomCommands]

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
    #
    # The format of a valid command is:
    # [command, what gets printed, the new location]
    def processCommand(generalCommands, locations, locationDescriptions,
                       locationCommands):
        # Some initial stuff specific to this loop
        score = 0
        locationIndex = 0
        playGame = True
        validCommand = False
        visitedLocations = []

        while playGame:
            # Should fire once every time entering a new location
            currentLocation = locations[locationIndex]  # Simple string
            validCommands = locationCommands[locationIndex]
            print()
            print()
            print(locationDescriptions[locationIndex])

            # Adds 5 points if you have not visited the location before.
            if currentLocation not in visitedLocations:
                score += 5
                visitedLocations.append(currentLocation)

            print("Your score is", score)

            # If you win, exit both loops.
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
                    # Prints every third item, the commands
                    for i in range(0, len(validCommands), 3):
                        print(validCommands[i])
                    print("▲--------▲")

                elif command in validCommands:
                    # Finds the index of the command.
                    i = validCommands.index(command)
                    print()
                    # Prints the description (the index after the command)
                    print(validCommands[i+1])

                    # If the item after that is not "None", break the loop
                    if(validCommands[i+2]):
                        validCommand = True
                        # Sets the new location index to be the same as
                        # the new location.
                        locationIndex = locations.index(validCommands[i+2])
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

from player import player
from location import location


# for item in bedroom.commands:
#     print(item)
#     print(bedroom.commands[item])
# print("1" in item)
# print("2" in item)


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

    def gameLoop():
        print(type(bedroom) is location)
        #Print only location
        #Print possible commands (also inventory, help, quit)
        #Check for being valid (while loop)
        #If it is a room
            #run goto function
        #If it is an item:
            #If it doesn't appear in inventory
                #Print message
            #Else
                #Add to inventory
            #Remove the command
        #If open inventory:
            #Print inventory
            #Get input
        #If quit:
            #Quit
        #If help:
            #Print help
        #If points
            #Print points
        #If map
            #Print map

    

    gameLoop()

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

# This is my semester-long project:
# a text-based adventure game in the spirit of Zork, Adventure, etc.


def main():
    # Initialize some variables.
    score = 0
    locations = ["bedroom", "hallway", "stairway", "street"]
    currentLocation = 0

    print()
    print()
    # Welcome message
    print("Welcome to the Dark Zone")
    print("You wake up with no memories and the place is pitch black. You are terrified")

    # Print location and score
    print("You are standing in a",
          locations[currentLocation] + ". You start to hear foot step coming towards you" ". Your score is", score)
    input("Press enter to continue")

    # Moves to next location and increases score.
    currentLocation += 1
    score += 5
    print("You are run into a",
          locations[currentLocation] + ". Some whispers to you and tells you to get out" ". Your score is", score)
    input("Press enter to continue")

    currentLocation += 1
    score += 5
    print("You are end up in a",
          locations[currentLocation] + ". You tell yourself to find an exit but you are lost and don't know which stairway can lead to the exit" ". You see a little girl run down the stairway on your left and you decide to follow her" ". Your score is", score)
    input("Press enter to continue")

    currentLocation += 1
    score += 5
    print("You are standing in a",
          locations[currentLocation] + ". The little girl you followed has lead you outside" ". The little girl is waiting for you on the other side of the street" ". As you get closer, you reach out to her and check if she is okay" ". The little girl slowly opens her mouth and shows her sharp teeth and rips your arm off" ". You were never seen again" ". Your score is", score)
    input("Press enter to continue")

    currentLocation += 1
    score += 5

    print()
    # Ending message
    print("Thanks for playing.")
    print("Copyright 2019.  Email me at Colin.MacDonald1[at]marist.edu")


main()

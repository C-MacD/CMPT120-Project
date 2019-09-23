# This is my semester-long project:
# a text-based adventure game in the spirit of Zork, Adventure, etc.


def main():
    # Initialize some variables.
    score = 0
    locations = ["bedroom", "hallway", "stairway", "kitchen"]
    currentLocation = 0

    print()
    print()
    # Welcome message
    print("Welcome to the Game")
    print("You wake up with no memories and look around")

    # Print location and score
    print("You are standing in a",
          locations[currentLocation] + ". Your score is", score)
    input("Press enter to continue")

    # Moves to next location and increases score.
    currentLocation += 1
    score += 5
    print("You are standing in a",
          locations[currentLocation] + ". Your score is", score)
    input("Press enter to continue")

    currentLocation += 1
    score += 5
    print("You are standing in a",
          locations[currentLocation] + ". Your score is", score)
    input("Press enter to continue")

    currentLocation += 1
    score += 5
    print("You are standing in a",
          locations[currentLocation] + ". Your score is", score)
    input("Press enter to continue")

    currentLocation += 1
    score += 5

    print()
    # Ending message
    print("Thanks for playing.")
    print("Copyright 2019.  Email me at Colin.MacDonald1[at]marist.edu")


main()

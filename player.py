from location import Location
from item import Item


class Player():
    def __init__(self):
        self.name = "Player"
        self.inventory = []
        self.score = 0
        self.location = Location
        self.visitedLocations = []
        self.newLocation = False
        self.MAX_MOVES = 0  # TODO: Change this
        self.moves = 0

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setLocation(self, location):
        self.location = location
        if(self.location not in self.visitedLocations):
            self.newLocation = True
        self.visitedLocations.append(location)

    def getLocation(self):
        return self.location

    def hasVisited(self, location):
        if(location in self.visitedLocations):
            return True
        else:
            return False

    def increaseScore(self, amount):
        self.score += amount

    def getPoints(self):
        return str(self.score)

    def inNewLocation(self):
        """Once this is called, it sets the location
        to not being a new location.

        Returns:
            Bool -- True if new, False if visited before.
        """
        temp = self.newLocation
        self.newLocation = False
        return temp

    # Take item
    def addItem(self, item):
        self.inventory.append(item)

    def getInventory(self):
        temp = []
        for item in self.inventory:
            temp.append(item.getName())
        return temp

    def getMoves(self):
        return self.moves

    def increaseMoves(self, num):
        self.moves += num

    def useItem(self, item):
        Item.useItem(item)

    def dropItem(self, item):
        self.inventory.remove(item)

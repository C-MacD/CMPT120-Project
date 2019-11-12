from location import location
from item import itemClass


class player():
    def __init__(self):
        self.name = "Player"
        self.inventory = []
        self.score = 0
        self.location = location
        self.visitedLocations = []
        self.newLocation = False

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

    def addItem(self, item):
        self.inventory.append(item)

    def getInventory(self):
        temp = []
        for item in self.inventory:
            temp.append(item.getName())
        return temp

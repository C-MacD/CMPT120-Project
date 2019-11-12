from location import location


class player():
    def __init__(self):
        self.name = "Player"
        self.inventory = []
        self.score = 0
        self.location = location
        self.visitedLocations = []

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setLocation(self, location):
        self.location = location
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
        return self.score

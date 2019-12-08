class Location():
    def __init__(self, name):
        self.name = name
        self.description = ""
        self.commands = {}
        self.wasVisited = False
        self.wasSearched = False
        self.items = []

    def addCommands(self, dictionary):
        self.commands.update(dictionary)

    def setDescription(self, description):
        self.description = description

    def getDescription(self):
        return self.description

    def getCommands(self):
        return self.commands

    def getName(self):
        return self.name

    def setVisited(self, x):
        self.wasVisited = x

    def search(self):
        self.wasSearched = True

    def getSearched(self):
        return self.wasSearched

    def addItem(self, item):
        self.items.append(item)

    def removeItem(self, item):
        self.items.remove(item)

    def getItems(self):
        return self.items

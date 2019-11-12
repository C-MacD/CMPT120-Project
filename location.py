class location():
    def __init__(self, name):
        self.name = name
        self.description = ""
        self.commands = {}

    def addCommands(self, dictionary):
        self.commands.update(dictionary)

    def setDescription(self, description):
        self.description = description
    
    def getDescription(self):
        return self.description

    def getCommands(self):
        return self.commands
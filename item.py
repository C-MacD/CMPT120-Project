class Item():
    def __init__(self, name, message, numUses):
        self.name = name
        self.message = message
        self.numUses = numUses
        # -1 appear in inventory, infinite uses
        # 0 remove from inventory and show final message
        # 1+ appears in inventory

    def getMessage(self):
        return self.message

    def getName(self):
        return self.name

    def getUses(self):
        return self.numUses

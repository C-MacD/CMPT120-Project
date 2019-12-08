class Item():
    def __init__(self, name, numUses, pickupMessage, useMessage):
        self.name = name
        self.numUses = numUses
        self.pickupMessage = pickupMessage
        self.useMessage = useMessage

        # -1 appear in inventory, infinite uses
        # 0 remove from inventory and show final message
        # 1+ appears in inventory

    def getPickupMessage(self):
        return self.pickupMessage

    def getName(self):
        return self.name

    def getUses(self):
        return self.numUses

    def useItem(self):
        if (self.numUses == -1):
            pass
        else:
            self.numUses -= 1

        print(self.useMessage)

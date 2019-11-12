class itemClass():
    def __init__(self, name, message, appearsInInventory, dissapearsOnUse):
        self.name = name
        self.message = message
        self.appearsInInventory = appearsInInventory
        self.dissapearsOnUse = dissapearsOnUse

    def shouldAppearInInventory(self):
        return self.appearsInInventory

    def getMessage(self):
        return self.message

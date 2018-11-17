class Cookbook:
    def __init__(self):
        self.__recipes = []
        self.__grocerylist = []

    def addrecipetogrocerylist(self, recipe):
        self.__grocerylist.append(self.__recipes[recipe])

    def getrecipe(self):
        
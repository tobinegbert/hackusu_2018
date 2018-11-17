class Recipe:
    def __init__(self, name="Air"):
        self.__ingredients = []
        self.__name = name

    def addIngredient(self, ingredient):
        self.__ingredients.append(ingredient)

    def getAllIngredients(self):
        return self.__ingredients

    def getIngredient(self, index):
        return self.__ingredients[index]

    def getName(self):
        return self.__name


class Cookbook:
    def __init__(self):
        self.__recipes = []
        self.__groceryList = []

    def getCookbook(self):
        return self.__recipes

    def addRecipe(self, recipe):
        self.__recipes.append(recipe)

    def getRecipe(self, index):
        return self.__recipes[index]

    def addToGroceryList(self, index):
        self.__groceryList.append(self.__recipes[index])

    def removeFromGroceryList(self, index):
        self.__groceryList.remove(self.__recipes[index])

    def getGroceryList(self):
        return self.__groceryList


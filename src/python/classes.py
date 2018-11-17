class Recipe:
    def __init__(self):
        self.__ingredients = []

    def addIngredient(self, ingredient, quantity):
        self.__ingredients.append(ingredient)

    def getIngredient(self):
        return self.__ingredients


class Cookbook:
    def __init__(self):
        self.__recipes = []

    def addRecipe(self, recipe):
        self.__recipes.append(recipe)


class ShoppingList:
    def __init__(self):
        self.__ingredients = []

    def addIngredient(self, ingredient):
        self.__ingredients.append(ingredient)

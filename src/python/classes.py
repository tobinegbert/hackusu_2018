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

        bread = Recipe("Bread")
        breadRecipe = ["flour:3.25:cup", "salt:.75:teaspoon", "yeast:.25:ounce", "water:1.25:cup"]
        bread.addIngredient(breadRecipe)

        crepe = Recipe("Crepes")
        crepeRecipe = ["flour:1:cup", "egg:2", "milk:.5:cup", "water:.5:cup", "salt:.25:teaspoon",
                       "butterMelted:2:tablespoons"]
        crepe.addIngredient(crepeRecipe)

        pancake = Recipe("Pancakes")
        pancakeRecipe = ["flout:1.5:cup", "bakingPowder:3.5:teaspoon", "sugar:1:tablespoon", "milk:1.25:cup",
                         "egg:1", "butterMelted:3:tablespoons"]
        pancake.addIngredient(pancakeRecipe)

        self.__recipes = [bread, crepe, pancake]
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


cookbook = Cookbook()
for i in range(len(cookbook.getCookbook())):
    print(cookbook.getRecipe(i).getName())
    print(cookbook.getRecipe(i).getAllIngredients())

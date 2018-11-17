from src.python.classes import Recipe
from src.python.classes import Cookbook


def main():

    cookbook = Cookbook()

    bread = Recipe("Bread")
    breadRecipe = ["3 and 1/4 cups of Flour", "3/4 Teaspoons of Salt", "1 package (1/4 ounce) of Yeast",
                   "1 and 1/4 cups of Water"]
    bread.addIngredient(breadRecipe)

    crepe = Recipe("Crepes")
    crepeRecipe = ["1 cup of Flour", "2 Eggs", "1/2 cup of Milk", "1/2 cup of Water", "1/4 teaspoon of Salt",
                   "2 tablespoons of Butter (melted)"]
    crepe.addIngredient(crepeRecipe)

    pancake = Recipe("Pancakes")
    pancakeRecipe = ["1 and 1/2 cups of Flour", "3 and 1/2 teaspoons of Baking Powder", "1 tablespoon of Sugar",
                     "1 and 1/4 cups of Milk", "1 Egg", "# tablespoons of Butter (melted)"]
    pancake.addIngredient(pancakeRecipe)

    cookbook.addRecipe(bread)
    cookbook.addRecipe(crepe)
    cookbook.addRecipe(pancake)

    done = False

    while not done:
        print("Choose a Recipe:")
        for i in range(len(cookbook.getCookbook())):
            print(str(i + 1) + ") " + str(cookbook.getRecipe(i).getName()))

        print(str(len(cookbook.getCookbook()) + 1) + ") Make your own Recipe!")
        print(str(len(cookbook.getCookbook()) + 2) + ") Exit")

        userChoice = eval(input(""))

        if userChoice <= len(cookbook.getCookbook()):
            print(str(cookbook.getRecipe(userChoice - 1).getName()) + ":")
            for i in range(len(cookbook.getRecipe(userChoice - 1).getAllIngredients())):
                print(cookbook.getRecipe(userChoice - 1).getIngredient(i))
        elif userChoice == len(cookbook.getCookbook()) + 1:
            newRecipe = Recipe(input("Name your recipe: "))
            newRecipeIngredients = []

            adding = True
            while adding:
                userIngredient = input("Add an ingredient, or press 1 to exit and add to cookbook: ")
                if userIngredient.strip() == "1":
                    break
                else:
                    newRecipeIngredients.append(userIngredient)

            cookbook.addRecipe(newRecipe)
            print(len(cookbook.getCookbook()))
        elif userChoice == len(cookbook.getCookbook()) + 2:
            print("Thanks!")
            break
        else:
            print("Choose again")


main()

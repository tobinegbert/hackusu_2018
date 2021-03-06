from src.python.classes import Recipe
from src.python.classes import Cookbook


def main():
    # Setting up basic cookbook list
    cookbook = Cookbook()

    # Default built-in recipes
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

    # Adding the default recipes to the cookbook
    cookbook.addRecipe(bread)
    cookbook.addRecipe(crepe)
    cookbook.addRecipe(pancake)

    # Main menu
    inMenu = True

    while inMenu:
        print("Welcome to your cookbook! What would you like to do?")
        options = ["View Recipes", "Grocery List", "Exit"]
        for i in range(len(options)):
            print(str(i + 1) + ") " + str(options[i]))

        menuChoice = eval(input(""))
        if menuChoice == 1:

            # Displaying the cookbook menu. Goes through cookbook list and labels each recipe with the getName method
            done = False

            while not done:
                print("Choose a Recipe:")
                for i in range(len(cookbook.getCookbook())):
                    print(str(i + 1) + ") " + str(cookbook.getRecipe(i).getName()))

                print(str(len(cookbook.getCookbook()) + 1) + ") Make your own Recipe!")
                print(str(len(cookbook.getCookbook()) + 2) + ") Return to Main Menu")

                userChoice = eval(input(""))

                # If user selects one of the listed recipes it displays the ingredients
                if userChoice <= len(cookbook.getCookbook()):
                    print(str(cookbook.getRecipe(userChoice - 1).getName()) + ":")
                    for i in range(len(cookbook.getRecipe(userChoice - 1).getAllIngredients())):
                        print(cookbook.getRecipe(userChoice - 1).getIngredient(i))

                # User makes their own recipe (custom name and ingredients)
                elif userChoice == len(cookbook.getCookbook()) + 1:
                    newRecipe = Recipe(input("Name your recipe: "))
                    newRecipeIngredients = []

                    # Adding ingredients
                    adding = True
                    while adding:
                        userIngredient = input("Add an ingredient, or press 1 to exit and add"
                                               " to cookbook: ").lower().strip()
                        if userIngredient.strip() == "1":
                            break
                        else:
                            userIngredient += ":" + input("What measurement?(cup, tsp, etc): ").lower().strip() + ":"
                            userIngredient += input("How much?: ").lower().strip()
                            newRecipeIngredients.append(userIngredient)

                    # Adding new user recipe to cookbook list
                    newRecipe.addIngredient(newRecipeIngredients)
                    cookbook.addRecipe(newRecipe)
                elif userChoice == len(cookbook.getCookbook()) + 2:
                    break
                else:
                    print("Choose again.")

        # Adding items to grocery list
        elif menuChoice == 2:

            # Groceries Menu
            inGroceries = True
            while inGroceries:
                print("What would you like to do?\n1) Add/Remove Items\n2) View Grocery List\n3) Return to main menu")
                userChoice = eval(input(""))

                # Adding or Removing Items to list
                if userChoice == 1:
                    addRemove = eval(input("1) Add\n2) Remove"))
                    if addRemove == 1:
                        print("Which recipe would you like to add items from?")
                        for i in range(len(cookbook.getCookbook())):
                            print(str(i + 1) + ") " + str(cookbook.getRecipe(i).getName()))
                        recipeChoice = eval(input("")) - 1
                        cookbook.addToGroceryList(recipeChoice)
                    elif addRemove == 2:
                        print("What items would you like to remove?")
                        for i in range(len(cookbook.getCookbook())):
                            print(str(i + 1) + ") " + str(cookbook.getRecipe(i).getName()))
                        recipeChoice = eval(input("")) - 1
                        cookbook.removeFromGroceryList(recipeChoice)

                # Displaying all items on the grocery list
                elif userChoice == 2:
                    print("Grocery List:")
                    for i in range(len(cookbook.getGroceryList())):
                        print(cookbook.getGroceryList()[i].getAllIngredients())

                # Exit groceries menu
                elif userChoice == 3:
                    break
                else:
                    print("Choose again.")

        # Exits the cookbook
        elif menuChoice == 3:
                print("Thanks!")
                break
        else:
            print("Choose again")


main()

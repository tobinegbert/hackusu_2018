import classes
import xml


def main():

    ingredient = input("Enter an ingredient: ")
    quantity = eval(input("Enter a quantity: "))

    classes.Recipe(ingredient, quantity)


main()

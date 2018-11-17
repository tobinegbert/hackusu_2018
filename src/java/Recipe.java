public class Recipe {
    private Ingredient LinkedList;

    public Recipe(Ingredient first) {
        this.LinkedList = first;
    }

    public void addIngredient(Ingredient ingredient) {
        LinkedList.setNext(ingredient);
    }
}

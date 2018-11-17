public class Ingredient {

    private String name;
    private float quantity;
    private Ingredient next;

    public Ingredient(String name, float quantity) {

        this.name = name;
        this.quantity = quantity;

    }

    public String getName() {
        return name;
    }

    public float getQuantity() {
        return quantity;
    }

    public void setNext(Ingredient next) {
        recSetNext(this.next, next);
    }

    private void recSetNext(Ingredient current, Ingredient next) {
        if(current == null) this.next = next;
        else recSetNext(current, next);
    }
}
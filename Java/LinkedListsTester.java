package LinkedLists.Java;

public class LinkedListsTester {
    public static void main(String[] args) {
        LinkedLists<Object> linkedLists = new LinkedLists<>();
        linkedLists.insertMiddle(0, 70);
        linkedLists.insertFirst(1);
        linkedLists.insertFirst(2);
        linkedLists.insertLast(3);
        linkedLists.insertLast(6);
        linkedLists.insertFirst(7);
        linkedLists.insertMiddle(1, 80);
        linkedLists.insertLast("Monkey");

        System.out.println("First: " + linkedLists.getFirst());
        System.out.println("Last: " + linkedLists.getLast());
        System.out.println("3: " + linkedLists.getValueFromIndex(3));
        System.out.println("Length: " + linkedLists.getLength());
        System.out.println("List: " + linkedLists.getStringList());

        linkedLists.removeFirst();
        linkedLists.removeFirst();

        System.out.println("List: " + linkedLists.getStringList());
        linkedLists.removeFromIndex(3);

        System.out.println("List: " + linkedLists.getStringList());
        System.out.println("ArrayList: " + linkedLists.getArrayList());
    }
}

package LinkedLists.Java;

public class Node<T> {
    T value;
    Node<T> next;
    Node<T> prev;

    public Node(T data) {
        value = data;
        next = null;
        prev = null;
    }
}

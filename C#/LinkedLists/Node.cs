public class Node<T>
{
    public T? value;
    public Node<T>? next;
    public Node<T>? prev;

    public Node(T data)
    {
        value = data;
        next = default(Node<T>);
        prev = default(Node<T>);
    }
}
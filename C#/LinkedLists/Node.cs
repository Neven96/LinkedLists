public class Node<T>
{
    public T? value { get; set; }
    public Node<T>? next { get; set; }
    public Node<T>? prev { get; set; }

    public Node(T data)
    {
        value = data;
        next = default(Node<T>);
        prev = default(Node<T>);
    }
}
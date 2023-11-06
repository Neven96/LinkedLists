public class LinkedLists<T>
{
    Node<T>? head;
    Node<T>? tail;

    int len;

    public LinkedLists()
    {
        this.head = default(Node<T>);
        this.tail = default(Node<T>);
        this.len = 0;
    }

    //
    //
    // INSERT NODES
    //
    //
    public void InsertFirst(T data)
    {
        Node<T>? new_node;
        Node<T>? current_node;

        new_node = new Node<T>(data);
        if (this.head == null)
        {
            this.head = new_node;
            this.tail = new_node;
        }
        else
        {
            current_node = this.head;
            new_node.next = current_node;
            current_node.prev = new_node;
            this.head = new_node;
        }

        this.len++;
    }

    public void InsertLast(T data)
    {
        Node<T>? new_node;
        Node<T>? current_node;

        new_node = new Node<T>(data);
        if (this.head == null)
        {
            this.head = new_node;
            this.tail = new_node;
        }
        else
        {
            current_node = this.tail;
            new_node.prev = current_node;
            current_node.next = new_node;
            this.tail = new_node;
        }

        this.len++;
    }

    public void InsertMiddle(int index, T data)
    {
        Node<T>? new_node;
        Node<T>? prev_node;
        Node<T>? next_node;

        if (this.head == null && index > 0)
        {
            throw new NullReferenceException("List is empty, so index is out of bounds!");
        }
        if ((index > this.len && this.len > 1) || index < 0)
        {
            throw new IndexOutOfRangeException("Index is out of bounds!");
        }
        if (index == 0)
        {
            InsertFirst(data);
            return;
        }
        if (index == this.len)
        {
            InsertLast(data);
            return;
        }

        new_node = new Node<T>(data);

        int count = 0;

        prev_node = this.head;
        while (index - 1 > count)
        {
            prev_node = prev_node.next;
            count++;
        }

        next_node = prev_node.next;

        // Sets the next and previous for the new_node
        new_node.prev = prev_node;
        new_node.next = next_node;

        // Sets the new_node as next and prev for their respective next and prev nodes
        prev_node.next = new_node;
        next_node.prev = new_node;

        this.len++;
    }

    //
    //
    // REMOVE NODES
    //
    //
    public void RemoveFirst()
    {
        Node<T>? deleted_node;
        Node<T>? next_node;

        if (this.head == null)
        {
            throw new NullReferenceException("List is empty!");
        }

        if (this.len == 1) {
            this.head = null;
            this.tail = null;
        } else {
            deleted_node = this.head;
            next_node = deleted_node.next;
            deleted_node.next = null;
            next_node.prev = null;
            this.head = next_node;
        }

        this.len--;
    }

    public void RemoveLast()
    {
        Node<T>? deleted_node;
        Node<T>? prev_node;

        if (this.head == null)
        {
            throw new NullReferenceException("List is empty!");
        }

        if (this.len == 1)
        {
            this.head = null;
            this.tail = null;
        }
        else
        {
            deleted_node = this.tail;
            prev_node = deleted_node.prev;
            prev_node.next = null;
            deleted_node.prev = null;
            this.tail = prev_node;
        }

        this.len--;
    }

    public void RemoveFromIndex(int index)
    {
        Node<T>? deleted_node;
        Node<T>? prev_node;
        Node<T>? next_node;

        if (this.head == null)
        {
            throw new NullReferenceException("List is empty!");
        }
        if (index >= this.len || index < 0)
        {
            throw new IndexOutOfRangeException("Index is out of bounds!");
        }
        if (index == 0)
        {
            RemoveFirst();
            return;
        }
        if (index == this.len - 1)
        {
            RemoveLast();
            return;
        }

        prev_node = this.head;

        int count = 0;

        while (index - 1 > count)
        {
            prev_node = prev_node.next;
            count++;
        }

        deleted_node = prev_node.next;
        next_node = deleted_node.next;

        deleted_node.prev = null;
        deleted_node.next = null;

        next_node.prev = prev_node;
        prev_node.next = next_node;

        this.len--;
    }

    //
    //
    // GET NODES
    //
    //
    public T GetFirst()
    {
        if (this.head == null)
        {
            throw new NullReferenceException("List is empty!");
        }

        return this.head.value;
    }

    public T GetLast()
    {
        if (this.head == null)
        {
            throw new NullReferenceException("List is empty!");
        }

        return this.tail.value;
    }

    public T GetFromIndex(int index)
    {
        Node<T>? current_node;

        if (this.head == null)
        {
            throw new NullReferenceException("List is empty!");
        }
        if (index >= this.len || index < 0)
        {
            throw new IndexOutOfRangeException("Index is out of bounds!");
        }
        if (index == 0)
        {
            return GetFirst();
        }
        if (index == this.len - 1)
        {
            return GetLast();
        }

        current_node = this.head;

        int count = 0;

        while (index > count)
        {
            current_node = current_node.next;
            count++;
        }

        return current_node.value;
    }

    public int GetLength() 
    {
        return this.len;
    }

    // Returns list as string
    public string ReturnStringList()
    {
        Node<T>? current_node;

        if (this.head == null)
        {
            throw new NullReferenceException("List is empty!");
        }

        string? out_string = "";
        out_string += "[";

        current_node = this.head;
        out_string += current_node.value.ToString();
        while (current_node.next != null)
        {
            current_node = current_node.next;
            out_string += ", ";
            out_string += current_node.value.ToString();
        }

        out_string += "]";
        return out_string;
    }

    public List<object> ReturnActualList() 
    {
        Node<T>? current_node;
        List<object> out_list = new List<object>();

        if (this.head == null)
        {
            throw new NullReferenceException("List is empty!");
        }

        current_node = this.head;

        out_list.Add(current_node.value);

        while (current_node.next != null)
        {
            current_node = current_node.next;
            out_list.Add(current_node.value);
        }

        return out_list;
    }
}
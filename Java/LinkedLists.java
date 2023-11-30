package LinkedLists.Java;
import java.util.ArrayList;
import java.util.List;

public class LinkedLists<T> {
    Node<T> head;
    Node<T> tail;
    int len;

    public LinkedLists() {
        head = null;
        tail = null;
        len = 0;
    }

    //
    //
    // INSERT NODES
    //
    //
    void insertFirst(T data) {
        Node<T> new_node;
        Node<T> current_node;

        new_node = new Node<T>(data);
        if (this.head == null) {
            this.head = new_node;
            this.tail = new_node;
        } else {
            current_node = this.head;
            new_node.next = current_node;
            current_node.prev = new_node;
            this.head = new_node;
        }

        this.len++;
    }

    void insertLast(T data) {
        Node<T> new_node;
        Node<T> current_node;

        new_node = new Node<T>(data);
        if (this.head == null) {
            this.head = new_node;
            this.tail = new_node;
        } else {
            current_node = this.tail;
            new_node.prev = current_node;
            current_node.next = new_node;
            this.tail = new_node;
        }

        this.len++;
    }

    void insertMiddle(int index, T data) {
        Node<T> new_node;
        Node<T> prev_node;
        Node<T> next_node;

        if (this.head == null && index > 0) {
            throw new NullPointerException("List is empty, so index is out of bounds!");
        }
        if ((index > this.len && this.len > 1) || index < 0) {
            throw new ArrayIndexOutOfBoundsException("Index is out of bounds!");
        }
        if (index == 0) {
            insertFirst(data);
            return;
        }
        if (index == this.len) {
            insertLast(data);
            return;
        }
        
        new_node = new Node<T>(data);

        int count = 0;

        prev_node = this.head;
        while (index-1 > count) {
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
    void removeFirst() {
        Node<T> deleted_node;
        Node<T> next_node;

        if (this.head == null) {
            throw new NullPointerException("List is empty!");
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

    void removeLast() {
        Node<T> deleted_node;
        Node<T> prev_node;

        if (this.head == null) {
            throw new NullPointerException("List is empty!");
        }

        if (this.len == 1) {
            this.head = null;
            this.tail = null;
        } else {
            deleted_node = this.tail;
            prev_node = deleted_node.prev;

            deleted_node.prev = null;
            prev_node.next = null;

            this.tail = prev_node;
        }
        
        this.len--;
    }

    void removeFromIndex(int index) {
        Node<T> deleted_node;
        Node<T> prev_node;
        Node<T> next_node;

        if (this.head == null) {
            throw new NullPointerException("List is empty!");
        }
        if (index >= this.len || index < 0) {
            throw new ArrayIndexOutOfBoundsException("Index is out of bounds!");
        }
        if (index == 0) {
            removeFirst();
            return;
        }
        if (index == this.len-1) {
            removeLast();
            return;
        }

        prev_node = this.head;

        int count = 0;

        while (index-1 > count) {
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
    // GET NODE VALUES
    //
    //
    T getFirst() {
        if (this.head == null) {
            throw new NullPointerException("List is empty!");
        }
        return this.head.value;
    }

    T getLast() {
        if (this.head == null) {
            throw new NullPointerException("List is empty!");
        }
        return this.tail.value;
    }

    T getValueFromIndex(int index) {
        Node<T> current_node;

        if (this.head == null) {
            throw new NullPointerException("List is empty!");
        }
        if (index >= this.len || index < 0) {
            throw new ArrayIndexOutOfBoundsException("Index is out of bounds!");
        }
        if (index == 0) {
            return getFirst();      
        }
        if (index == this.len-1) {
            return getLast();  
        }

        current_node = this.head;

        int count = 0;

        while (index > count) {
            current_node = current_node.next;
            count++;
        }

        return current_node.value;
    }

    int getLength() {
        return this.len;
    }

    // Returns the entire list as a String looking like an array
    String getStringList() {
        Node<T> current_node;
        String out_string;

        if (this.head == null) {
            throw new NullPointerException("List is empty!");
        }

        out_string = "[";
        
        current_node = this.head;
        out_string += String.valueOf(current_node.value);
        while (current_node.next != null) {
            current_node = current_node.next;
            out_string += ", ";
            out_string += String.valueOf(current_node.value);
        }

        out_string += "]";

        return out_string;
    }

    // Creates an ArrayList of the LinkedList and returns it
    List<Object> getArrayList() {
        Node<T> current_node;
        List<Object> outArray = new ArrayList<>();

        if (this.head == null) {
            throw new NullPointerException("List is empty!");
        }

        current_node = this.head;
        outArray.add(current_node.value);
        while (current_node.next != null) {
            current_node = current_node.next;
            outArray.add(current_node.value);
        }

        return outArray;
    }

    // Prints the entire list, line by line
    void printLinkedList() {
        Node<T> current_node;

        if (this.head == null) {
            throw new NullPointerException("List is empty!");
        }
        current_node = this.head;
        System.out.println(current_node.value);
        while (current_node.next != null) {
            current_node = current_node.next;
            System.out.println(current_node.value);
        }
    }
}
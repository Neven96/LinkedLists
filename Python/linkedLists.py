class Node:
    def __init__(self, data):
        """
        Initializes a Node element with value data and empty next and prev.

        Args:
            data: any type of data you want in the node. 
        """

        self.value = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        """
        Initialize an empty LinkedList object with no set head or tail and a length of 0.
        """

        self.head = None
        self.tail = None
        self.length = 0

    # 
    # 
    # INSERT NODES
    # 
    # 
    def insertFirst(self, data) -> None:
        """
        Inserts Node at the front of the list.

        Args:
            data: any type of data you want in the node.
        """

        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        self.length += 1

    def insertLast(self, data) -> None:
        """
        Inserts Node at the back of the list.

        Args:
            data: any type of data you want in the node.
        """

        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1

    def insertMiddle(self, index, data) -> None:
        """
        Inserts Node at the stated index in the list.

        Args:
            index: the position of the new Node, 0 is the first position.
            data: any type of data you want in the node.
        Raises:
            IndexError: If the stated index is negative or bigger than the length of the list.
        """

        new_node = Node(data)

        if self.head is None and index > 0:
            raise IndexError("List is empty, index out of bounds")
        if (index > self.length and self.length > 0) or index < 0:
            raise IndexError("Index out of bounds")
        if index == 0:
            self.insertFirst(data)
        if index == self.length:
            self.insertLast(data)

        count = 0
        prev_node = self.head

        while index-1 > count:
            prev_node = prev_node.next
            count += 1

        next_node = prev_node.next

        new_node.prev = prev_node
        new_node.next = next_node

        prev_node.next = new_node
        next_node.prev = new_node

        self.length += 1

    # 
    # 
    # REMOVE NODES
    # 
    # 
    def removeFirst(self) -> None:
        """
        Removes the node at the front of the list.
        """

        if self.head is None:
            raise IndexError("List is empty")
        
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            deleted_node = self.head
            next_node = deleted_node.next

            deleted_node.next = None
            next_node.prev = None

            self.head = next_node

        self.length -= 1
        
    
    def removeLast(self) -> None:
        """
        Removes the node at the back of the list.
        """

        if self.head is None:
            raise IndexError("List is empty")
        
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            deleted_node = self.tail
            prev_node = deleted_node.prev

            deleted_node.prev = None
            prev_node.next = None

            self.tail = prev_node

        self.length -= 1
    
    def removeFromIndex(self, index) -> None:
        """
        Removes the node at stated index of the list.

        Args:
            index: the index of the deleted Node, 0 is the first position.
        """

        if self.head is None and index > 0:
            raise IndexError("List is empty, index out of bounds")
        if (index > self.length and self.length > 0) or index < 0:
            raise IndexError("Index out of bounds")
        if index == 0:
            self.removeFirst()
        if index == self.length-1:
            self.removeLast()

        prev_node = self.head

        count = 0

        while index-1 > count:
            prev_node = prev_node.next
            count += 1

        deleted_node = prev_node.next
        next_node = deleted_node.next

        deleted_node.prev = None
        deleted_node.next = None

        next_node.prev = prev_node
        prev_node.next = next_node

        self.length -= 1

    # 
    # 
    # GET NODE VALUES
    # 
    # 
    def getFirst(self) -> any:
        """
        Returns the head value of the list.

        Return:
            Variable: value of the head Node.
        """

        if self.head is None:
            raise IndexError("List is empty")
        
        return self.head.value
    
    def getLast(self) -> any:
        """
        Returns the tail value of the list.

        Returns:
            Variable: value of the tail Node.
        """

        if self.head is None:
            raise IndexError("List is empty")
        
        return self.tail.value
    
    def getValueFromIndex(self, index) -> any:
        """
        Returns the value of the Node from the stated index.

        Args:
            index: the index of the Node you want to get the value from, list starts at 0.

        Returns:
            Variable: value of the Node at the stated index.
        """

        if self.head is None and index > 0:
            raise IndexError("List is empty, index out of bounds")
        if (index > self.length and self.length > 0) or index < 0:
            raise IndexError("Index out of bounds")
        if index == 0:
            return self.getFirst()
        if index == self.length-1:
            return self.getLast()
        
        current_node = self.head

        count = 0

        while index > count:
            current_node = current_node.next
            count += 1

        return current_node.value
    
    def getLength(self) -> int:
        """
        Returns the length of the list

        Returns:
            int: the length of the LinkedList
        """
        return self.length
    
    def __str__(self) -> str:
        """
        Returns an array of the values in the list

        Returns:
            str: a string looking like an array, not actual array.
        """

        if self.head == None:
            raise IndexError("List is empty")

        out_string = "["
        out_string += str(self.head.value)

        current_node = self.head

        while current_node.next is not None:
            current_node = current_node.next
            out_string += ", "
            out_string += str(current_node.value)

        out_string += "]"

        return out_string


if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.insertFirst(1)
    linked_list.insertFirst(2)
    linked_list.insertLast(9)
    print(linked_list.getFirst())
    print(linked_list)
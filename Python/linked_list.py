from node import Node

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
    # SETTERS
    # 
    # 
    def set_head(self, node: object) -> None:
        self.head = node

    def set_tail(self, node: object) -> None:
        self.tail = node

    # 
    # 
    # LENGTH MANIPULATION
    # 
    # 
    def increase_length(self) -> None:
        self.length += 1

    def decrease_length(self) -> None:
        self.length -= 1

    # 
    # 
    # INSERT NODES
    # 
    # 
    def insert_first(self, data: any) -> None:
        """
        Inserts Node at the front of the list.

        Args:
            data: any type of data you want in the node.
        """

        new_node = Node(data)

        if self.head is None:
            self.set_head(new_node)
            self.set_tail(new_node)
        else:
            new_node.set_next(self.head)
            self.head.set_prev(new_node)
            self.set_head(new_node)

        self.increase_length()

    def insert_last(self, data: any) -> None:
        """
        Inserts Node at the back of the list.

        Args:
            data: any type of data you want in the node.
        """

        new_node = Node(data)

        if self.head is None:
            self.set_head(new_node)
            self.set_tail(new_node)
        else:
            new_node.set_prev(self.tail)
            self.tail.set_next(new_node)
            self.set_tail(new_node)

        self.increase_length()

    def insert_middle(self, index: int, data: any) -> None:
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
            self.insert_first(data)
            return
        if index == self.length:
            self.insert_last(data)
            return

        count = 0
        prev_node = self.head

        while index-1 > count:
            prev_node = prev_node.next
            count += 1

        next_node = prev_node.next

        # Update next and prev
        new_node.set_next(next_node)
        new_node.set_prev(prev_node)

        prev_node.set_next(new_node)
        next_node.set_prev(new_node)

        self.increase_length()

    # 
    # 
    # REMOVE NODES
    # 
    # 
    def remove_first(self) -> None:
        """
        Removes the node at the front of the list.
        """

        if self.head is None:
            raise IndexError("List is empty")
        
        if self.length == 1:
            self.set_head(None)
            self.set_tail(None)
        else:
            deleted_node = self.head
            next_node = deleted_node.next

            deleted_node.set_next(None)
            next_node.set_prev(None)

            self.set_head(next_node)

        self.decrease_length()
        
    
    def remove_last(self) -> None:
        """
        Removes the node at the back of the list.
        """

        if self.head is None:
            raise IndexError("List is empty")
        
        if self.length == 1:
            self.set_head(None)
            self.set_tail(None)
        else:
            deleted_node = self.tail
            prev_node = deleted_node.prev

            deleted_node.set_prev(None)
            prev_node.set_next(None)

            self.set_tail(prev_node)

        self.decrease_length()
    
    def remove_from_index(self, index: int) -> None:
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
            self.remove_first()
            return
        if index == self.length-1:
            self.remove_last()
            return

        prev_node = self.head

        count = 0

        while index-1 > count:
            prev_node = prev_node.next
            count += 1

        deleted_node = prev_node.next
        next_node = deleted_node.next

        # Update next and prev
        deleted_node.set_next(None)
        deleted_node.set_prev(None)

        prev_node.set_next(next_node)
        next_node.set_prev(prev_node)

        self.decrease_length()

    # 
    # 
    # GET NODE VALUES
    # 
    # 
    def get_first(self) -> any:
        """
        Returns the head value of the list.

        Return:
            Variable: value of the head Node.
        """

        if self.head is None:
            raise IndexError("List is empty")
        
        return self.head.value
    
    def get_last(self) -> any:
        """
        Returns the tail value of the list.

        Returns:
            Variable: value of the tail Node.
        """

        if self.head is None:
            raise IndexError("List is empty")
        
        return self.tail.value
    
    def get_value_from_index(self, index: int) -> any:
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
            return self.get_first()
        if index == self.length-1:
            return self.get_last()
        
        current_node = self.head

        count = 0

        while index > count:
            current_node = current_node.next
            count += 1

        return current_node.value
    
    def __len__(self) -> int:
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
        
        current_node = self.head

        out_string = "["
        out_string += str(current_node.value)

        while current_node.next is not None:
            current_node = current_node.next
            out_string += ", "
            out_string += str(current_node.value)

        out_string += "]"

        return out_string
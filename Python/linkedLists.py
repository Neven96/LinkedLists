class Node:
    def __init__(self, data):
        self.value = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    # 
    # 
    # INSERT NODES
    # 
    # 
    def insertFirst(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insertLast(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def insertMiddle(self, index, data):
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

    # 
    # 
    # REMOVE NODES
    # 
    # 


    # 
    # 
    # GET NODE VALUES
    # 
    # 
    def getFirst(self):
        if self.head is None:
            raise IndexError("List is empty")
        
        return self.head.value
    
    def getLast(self):
        if self.head is None:
            raise IndexError("List is empty")
        
        return self.tail.value
            


if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.insertFirst(1)
    linked_list.insertFirst(2)
    linked_list.insertLast(9)
    print(linked_list.getFirst())
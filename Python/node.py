class Node:
    def __init__(self, data: any):
        """
        Initializes a Node element with value data and empty next and prev.

        Args:
            data: any type of data you want in the node. 
        """

        self.value = data
        self.next = None
        self.prev = None

    def set_next(self, node: object) -> None:
        self.next = node
    
    def set_prev(self, node: object) -> None:
        self.prev = node

    def __str__(self) -> str:
        return str(self.value)
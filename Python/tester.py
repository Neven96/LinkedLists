from linked_list import LinkedList

if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.insert_first(1)
    linked_list.insert_first(2)
    linked_list.insert_last(9)
    print(linked_list.get_first())
    print(linked_list.get_last())
    print(linked_list)
    print("Length: " + str(len(linked_list)))
    linked_list.insert_middle(2, 3)
    linked_list.insert_middle(0, 7)
    print(linked_list)
    linked_list.remove_last()
    print(linked_list)
    linked_list.remove_from_index(2)
    print(linked_list)
    
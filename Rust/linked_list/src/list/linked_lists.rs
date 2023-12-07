use crate::node::Node;

type Link<T> = Option<Box<Node<T>>>;

#[derive(Debug)]
pub struct LinkedList<T: std::clone::Clone> {
    pub head: Link<T>,
    pub tail: Link<T>,
    pub length: i32,
}

impl<T: std::clone::Clone> LinkedList<T> {
    pub fn new() -> Self {
        LinkedList {
            head: None,
            tail: None,
            length: 0,
        }
    }

    //
    //
    // INSERT NODES
    //
    //
    pub fn insert_first(&mut self, data: T) {
        let mut new_node = Node::new(data);
        match self.head.take() {
            Some(mut old_node) => {
                old_node.prev = Some(Box::new(new_node.clone()));
                new_node.next = Some(old_node);
                self.head = Some(Box::new(new_node));
            }
            None => {
                self.tail = Some(Box::new(new_node.clone()));
                self.head = Some(Box::new(new_node));
            }
        }

        self.length += 1;
    }

    pub fn insert_last(&mut self, data: T) {
        let mut new_node = Node::new(data);
        match self.tail.take() {
            Some(mut old_node) => {
                old_node.next = Some(Box::new(new_node.clone()));
                new_node.prev = Some(old_node);
                self.tail = Some(Box::new(new_node));
            }
            None => {
                self.tail = Some(Box::new(new_node.clone()));
                self.head = Some(Box::new(new_node));
            }
        }

        self.length += 1;
    }

    //
    //
    // GET NODES
    //
    //
    pub fn get_first(&mut self) -> Option<T> {
        match self.head.take() {
            Some(head_value) => {
                return Some(head_value.value);
            }
            None => {
                return None;
            }
        }
    }

    pub fn get_last(&mut self) -> Option<T> {
        match self.tail.take() {
            Some(tail_value) => {
                return Some(tail_value.value);
            }
            None => {
                return None;
            }
        }
    }
}
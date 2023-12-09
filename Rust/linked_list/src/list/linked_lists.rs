use crate::node::Node;

type Link<T> = Option<Box<Node<T>>>;

#[derive(Debug)]
pub struct LinkedList<T: std::clone::Clone> {
    pub head: Link<T>,
    pub tail: Link<T>,
    pub length: i32,
}

impl<T: std::clone::Clone + std::fmt::Debug> LinkedList<T> {
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
    // insert_first and insert_last does not "communicate" with eachother, 
    // so any insert_last does not become the next node for insert_first...
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
        match &self.head {
            Some(head_value) => {
                return Some(head_value.value.clone());
            }
            None => {
                return None;
            }
        }
    }

    pub fn get_last(&mut self) -> Option<T> {
        match &self.tail {
            Some(tail_value) => {
                return Some(tail_value.value.clone());
            }
            None => {
                return None;
            }
        }
    }

    pub fn get_list(&mut self) -> Vec<T> {
        let mut list_array = Vec::new();

        if self.length == 0 {
            panic!("List is empty")
        }

        if self.length > 0 {
            let mut current_node = self.get_actual_node(self.head.clone());
            list_array.push(current_node.value.clone());
            
            while current_node.next.is_some() {
                current_node = self.get_actual_node(current_node.next.clone());
                list_array.push(current_node.value.clone());
            }
            
        }

        return list_array;
    }

    //
    //
    // "HELPER" FUNCTIONS
    //
    //

    pub fn get_actual_node(&mut self, node: Option<Box<Node<T>>>) -> Node<T> {
        return Box::into_inner(<Option<Box<Node<T>>> as Clone>::clone(&node).expect("No Node"));
    }
}
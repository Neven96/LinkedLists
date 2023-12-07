type Link<T> = Option<Box<Node<T>>>;

#[derive(Debug, Clone)]
pub struct Node<T> where T: Clone {
    pub value: T,
    pub next: Link<T>,
    pub prev: Link<T>,
}

impl<T: std::clone::Clone> Node<T> {
    pub fn new(data: T) -> Self {
        Node {
            value: data,
            next: None,
            prev: None,
        }
    }
}
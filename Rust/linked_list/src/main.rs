#![feature(box_into_inner)]
use crate::list::linked_lists;
use crate::linked_lists::LinkedList;
use crate::list::node;
pub mod list;

fn main() {
    // let mut linked_list: linked_lists::LinkedList<i32> = LinkedList::new();
    // linked_list.insert_first(1);
}

#[cfg(test)]
mod test {
    use crate::list::linked_lists;
    use crate::linked_lists::LinkedList;

    // This works
    #[test]
    fn insert_first_tests() {
        let mut linked_list: linked_lists::LinkedList<i32> = LinkedList::new();
        linked_list.insert_first(5);
        linked_list.insert_first(7);
        linked_list.insert_first(6);
        assert_eq!(linked_list.get_list(), vec![6, 7, 5]);
    }

    // This does not work...
    #[test]
    fn insert_last_test() {
        let mut linked_list: linked_lists::LinkedList<i32> = LinkedList::new();
        linked_list.insert_last(5);
        linked_list.insert_last(7);
        linked_list.insert_last(6);
        assert_eq!(linked_list.get_list(), vec![5, 7, 6]);
    }
}
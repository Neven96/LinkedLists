#![feature(box_into_inner)]
use crate::list::linked_lists;
use crate::linked_lists::LinkedList;
use crate::list::node;

pub mod list;

fn main() {
    let mut linked_list: linked_lists::LinkedList<i32> = LinkedList::new();
    linked_list.insert_first(5);
    linked_list.insert_first(7);
    linked_list.insert_first(6);
    // println!("{:?}", linked_list);
    // println!("{:?}", linked_list.get_first());
    // println!("{:?}", linked_list.get_first());
    // println!("{:?}", linked_list.get_last());
    println!("{:?}", linked_list.get_list());
}

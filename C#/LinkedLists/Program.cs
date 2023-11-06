class Program {
    static void Main() {
        LinkedLists<object> ll = new LinkedLists<object>();
        ll.InsertFirst(3);
        ll.InsertFirst(4);
        ll.InsertLast(1);
        ll.InsertFirst(5);
        Console.WriteLine("First: " + ll.GetFirst());
        Console.WriteLine("List: " + ll.ReturnStringList());
        Console.WriteLine("Last: " + ll.GetLast());
        ll.InsertMiddle(2, "Man");
        Console.WriteLine("List: " + ll.ReturnStringList());
        ll.InsertMiddle(5, "Non");
        ll.InsertFirst(8);
        Console.WriteLine("List: " + ll.ReturnStringList());
        Console.WriteLine("Length: " + ll.GetLength());
        Console.WriteLine("Actual List: " + string.Join(", ", ll.ReturnActualList()));
        // List<object> acutalList = ll.ReturnActualList();
        // foreach (var item in acutalList)
        // {
        //     Console.WriteLine(item);
        // }
    }
}

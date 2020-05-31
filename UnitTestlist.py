from list import LinkedList

try:
    print(">>>>>>>>>>>>>>> Creating object of linked list <<<<<<<<<<<<<<<<")
    list = LinkedList()
    print("Test passed.\n")
    print(">>>>>>>>>>>>>>> Adding node to list <<<<<<<<<<<<<<<<")
    list.add_last("Woody")
    list.add_last("Jim")
    list.add_last("John")
    print("Test passed.\n")
    print(">>>>>>>>>>>>>>> Printing list <<<<<<<<<<<<<<<<")
    print(list)
    print("*|*|*|*|*|*|*|*|*|>>> ALL TEST PASSED <<<|*|*|*|*|*|*|*|*|*")
except Exception as e:
    print(e)
    print("Test Failed !")
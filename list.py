from node import Node


class LinkedList:
    """
    This is the ADT I have developed represents lists of nodes having a head, tail and a value.
    This value can again be a LinkedList
    """

    def __init__(self, value=None, head=None, tail=None):
        """
        Creates an object of class LinkedList
        :param value: value of the list
        :param head: head reference
        :param tail: tail reference
        """
        self.head = head  # head of list
        self.tail = tail  # tail of list
        self.value = value  # value of list

    def add_last(self, value):
        """
        Add the node to the last of the list
        :param value: value to be added
        :return: None
        """
        if self.head is None:  # if list is  empty
            self.head = self.tail = Node(value)
        else:  # if list is not empty
            n = Node(value, self.tail)  # create new node
            self.tail.next_node = n
            self.tail = n

    def find_node(self, node, link=0):
        """
        Finds a given node in the list
        :param node: Node to be found
        :param link: tells whether it is called on from list object or graph object
        :return: Node
        """
        n = self.head
        if link is 1:  # this link condition is when i call find_node to delete edge
            # and not the node from whole graph
            if self.head is not None:  # if list is not empty
                n = self.head.value
        while n:  # checks each node, compares it and return if matched
            if n.value.is_equal(node):
                return n
            n = n.next_node
        return None

    def delete_node(self, node, link=0):
        """
        Delete a given node from the linked list
        :param node: node to be deleted
        :param link: tells whether it is called on from list object or graph object
        :return: Deleted node's value
        """
        n = self.find_node(node)  # checks if the given node is even present in the graph or not
        if link is 1:  # this link condition is when i call find_node to delete edge
            # and not the node from whole graph
            n = self.find_node(node, 1)
        if n is not None:  # if node is present in the graph
            if self.head is self.tail:  # list has only one node
                self.head = self.tail = None
                return n.value
            elif n.prev_node is None:  # means node is first node
                self.head = self.head.next_node
                self.head.prev_node = None
                return n.value
            elif n.next_node is None:  # means node is last
                self.tail = self.tail.prev_node
                self.tail.next_node = None
                return n.value
            else:  # node is somewhere in middle of list
                n.prev_node.next_node = n.next_node
                n.next_node.prev_node = n.prev_node
                return n.value

    def is_equal(self, other):
        """
        Compares lists objects
        :param other: object by which self is compared to
        :return: true, False
        """
        return self.value == other if type(other) is type(self.value) else False

    def __str__(self):
        """
        Converts object of lits to string object
        :return: str
        """
        n, s = self.head, ""
        while n:
            if n.next_node is not None:  # so that we dont have unwanted "|-|" after last node
                s = s + str(n.value) + " |-| "
            else:
                s = s + str(n.value) + " "
            n = n.next_node
        return s
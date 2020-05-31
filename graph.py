from list import LinkedList


class Graph:
    """
    Simulates a complete network
    """

    def __init__(self):
        """
        Creates object to graph
        """
        self.list = LinkedList()

    def connect(self, v1, v2):
        """
        Create a connection between two persons
        :param v1: person1
        :param v2: person2
        :return: None
        """
        a = self.list.find_node(v1)  # searches for v1 in graph
        b = self.list.find_node(v2)  # searches for v2 in graph
        if a is None or b is None:  # if any of given node is not present then return
            return
        if not a.value.find_node(b.get_value()):  # if previsuy there is not connection then add connection
            a.value.add_last(b)
            a.flrs += 1  # increases number of folowers of node a
            b.fol += 1  # increase number of persons that node b follows

    def delete_node(self, node):
        """
        Delete node from the graph
        :param node: node to be deleted
        :return: None
        """
        n = self.list.head
        while n:
            n.value.delete_node(node,
                                1)  # given the link=1, so that LinkedList.delete_node will know that it has to delete edge
            n = n.next_node

    def delete_edge(self, node1, node2):
        """
        delete connection between two given persons
        :param node1: person1
        :param node2: person2
        :return: True, False
        """
        n = self.list.head
        state = False  # will return whether edge is delete or not
        while n:
            if n.value.delete_node(node2, 1) is not None:
                state = True
            if n.value.delete_node(node1, 1) is not None:
                state = True
            n = n.next_node
        return state

    def __str__(self):
        """
        Converts and object of graph to am object of string
        :return: string
        """
        n, s = self.list.head, ""
        while n:
            s = s + n.value.value + "--> " + str(n.get_value()) + "\n"
            n = n.next_node
        return s

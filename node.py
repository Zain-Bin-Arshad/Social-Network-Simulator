class Node:
    """
    Single person in the network
    """

    def __init__(self, value, prev_node=None, next_node=None):
        """
        Creates a new person
        :param value: value of the node
        :param prev_node: reference to previous node
        :param next_node: reference to next node
        """
        self.prev_node = prev_node
        self.next_node = next_node
        self.value = value
        self.posts = []  # posts of this person
        self.likes = 0  # total likes he got
        self.fol = 0  # number of person he is following
        self.flrs = 0  # number of persons following this person

    def get_value(self):
        """
        To get the value of the node
        :return: node.value
        """
        return self.value if type(self) is Node else self.value.value

    def is_equal(self, other):
        """
        Comparision for equality between nodes
        :param other: node compared to
        :return: True, False
        """
        if type(other) is type(self.value):
            return self.value.is_equal(other)
        elif type(other) is Node:
            return self.value.is_equal(other.value)
        else:
            return False

    def __str__(self):
        """
        Converts Node object to string object
        :return: str
        """
        return self.value if type(self.value) is str else self.value.value

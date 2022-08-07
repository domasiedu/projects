class Node:
    """
    An object to store a single node of a linked list.
    Models 2 attributes - data and the link to the next node in the list
    """
    data = None
    next_node = None

    def __init__(self, data):
        self.data = data
    def __repr__(self):
        return "Node data: %s>" % self.data

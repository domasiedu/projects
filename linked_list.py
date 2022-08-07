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
        return "Node data: %s>" % self.data     # "%s" is Python way of substituting something into a string.

    class LinkedList:
        """
        Singly Linked list
        """
        head = None

        def __init__(self):
            self.head = None

        def is_empty(self):
            return self.head == None

        def size(self):
            """
            Returns the number of nodes in the list
            Takes O(n) time
            """
            current = self.head
            count = 0

            while current:
                count += 1
                current = current.next_node
            return count

class Node:
    """
    An object to store a single node of a linked list.
    Models 2 attributes - data and the link to the next node in the list
    """
    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def search(self, key):
        """
        Search for te first node containing data that matches the key
        Return the node or None if not found

        Takes O(n) time
        """
        current = self.head

        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None

    def __repr__(self):

        nodes = []
        current = self.head

        while current:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)

            current = current.next_node
        return '->'.join(nodes)

        # return "Node data: %s>" % self.data  # "%s" is Python way of substituting something into a string.


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

    def add(self, data):
        """
            Adds New Node containing data at head of the list
            Takes O(1) time
            """
        new_node = Node(data)
        new_node.net_node = self.head
        self.head = new_node

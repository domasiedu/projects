from node import Node


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self, value):

        item_to_add = Node(value)
        print("Adding " + str(item_to_add.get_value()) + " to the queue!")
        if self.is_empty():
            self.head = item_to_add
            self.tail = item_to_add
            self.size = 1
        else:
            self.tail.set_next_node(item_to_add)
            self.tail = item_to_add
            self.size += 1

    def dequeue(self):
        if self.get_size() > 0:
            item_to_remove = self.head
            print(str(item_to_remove.get_value()) + " is served!")
            if self.get_size() == 1:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.get_next_node()
                self.size -= 1
                return item_to_remove.get_value()
        else:
            print("The queue is totally empty!")

    def peek(self):
        if self.size > 0:
            return self.head.get_value()
        else:
            print("No orders waiting!")

    def get_size(self):
        return self.size

    def is_empty(self):
        return self.size == 0


print("Creating a deli line with up to 10 orders...\n------------")
deli_line = Queue()
print("Adding orders to our deli line...\n------------")
deli_line.enqueue("egg and cheese on a roll")
deli_line.enqueue("bacon, egg, and cheese on a roll")
deli_line.enqueue("toasted sesame bagel with butter and jelly")
deli_line.enqueue("toasted roll with butter")
deli_line.enqueue("bacon, egg, and cheese on a plain bagel")
deli_line.enqueue("two fried eggs with home fries and ketchup")
deli_line.enqueue("egg and cheese on a roll with jalapeos")
deli_line.enqueue("plain bagel with plain cream cheese")
deli_line.enqueue("blueberry muffin toasted with butter")
deli_line.enqueue("bacon, egg, and cheese on a roll")
# ------------------------ #
# Uncomment the line below:
# deli_line.enqueue("western omelet with home fries")
# ------------------------ #
print("------------\n Our first order will be " + deli_line.peek())
print("------------\n Now serving...\n------------")
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()

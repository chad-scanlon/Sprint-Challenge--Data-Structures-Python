class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next
    # makes this node's next_node pointer to the node passed in
class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False
    # is empty to set the value as the head
        current = self.head

        while current:
            if current.get_value() == value:
                return True
    # check the value, return out if it is that value
            current = current.get_next()
    # move onto the next node 
    # loop runs again to check the value, which isn't there so return out of it
        return False

    def reverse_list(self, node, prev):
        if node == None:
            self.head = prev
            # is empty set the head attribute
        else:
            next_node = node.next_node
            # add a node to list 
            node.next_node = prev
            # move the pointer of the next node to become the previous node
            prev = node
            # prev becomes the head
            node = next_node
            # node passed in becomes the next node
            self.reverse_list(node, prev)
            
from Nodes import Node


class CircularlinkedList:  # list of nodes, in which the last one points to the first
    def __init__(self, r=None):
        self.root = r
        self.size = 0

    def get_root(self):  # bunch of get functions for ease of access
        return self.root

    def get_second(self):  # returns second node
        return self.root.next_node

    def get_third(self):  # returns third node
        this_node = self.root.next_node
        this_node = this_node.next_node
        return this_node

    def get_size(self):  # returns the size of the list
        return self.size

    def add(self, d=Node()):
        if self.size == 0:  # if empty create new
            self.root = Node(d)
            self.root.next_node = self.root
        else:  # else put it second
            new_node = Node(d, self.root.next_node)
            self.root.next_node = new_node
        self.size += 1

    def spin(self, times):  # function which rotates the list num of times
        if self.root is None:  # check if list is empty
            return
        if times == 0 or times % self.get_size() == 0:  # check if needed to rotate
            return
        prev_node = None  # works as a temporary node to store the current
        count = 0
        while count < times and self.root is not None:
            if prev_node is not None:
                prev_node = prev_node.next_node
            else:
                prev_node = self.root  # prev_node becomes the current and the current becomes its next
            self.root = self.root.next_node
            count += 1

    def copy(self, source):  # copy function from another list
        self.root = source.root
        self.size = source.size
        this_node = self.root
        source_node = source.get_root()
        while source_node.get_next_node() != source.get_root():  # copy until the last one pointing to the root
            source_node = source_node.get_next_node()
            this_node.next_node = source_node
            this_node = this_node.next_node
        this_node.next_node = self.root  # make it circular by pointing the last to the first

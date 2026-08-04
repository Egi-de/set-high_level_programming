#!/usr/bin/python3
"""Module that defines a Node and a SinglyLinkedList class."""


class Node:
    """Represents a node in a singly linked list."""

    def __init__(self, data, next_node=None):
        """Initialize a Node with data and an optional next_node."""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Return the data stored in this node."""
        return self.__data

    @data.setter
    def data(self, value):
        """Set the data, validating it is an integer."""
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Return the next node in the list."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set the next node, validating it is None or a Node."""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Represents a singly linked list of Nodes."""

    def __init__(self):
        """Initialize an empty SinglyLinkedList."""
        self.__head = None

    def sorted_insert(self, value):
        """Insert a new Node with value into the list, keeping it sorted."""
        new_node = Node(value)
        if self.__head is None or self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
            return
        current = self.__head
        while (current.next_node is not None and
               current.next_node.data < value):
            current = current.next_node
        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        """Return a string of all node values, one per line."""
        nodes = []
        current = self.__head
        while current is not None:
            nodes.append(str(current.data))
            current = current.next_node
        return "\n".join(nodes)

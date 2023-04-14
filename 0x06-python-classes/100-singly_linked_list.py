#!/usr/bin/python3
""" Sorted singlylinked list"""


class Node:
    """Class that defines a node"""

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")

        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")

        self.__next_node = value


class SinglyLinkedList:
    """Creates and prints a sorted singly linked list"""

    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):

        new = Node(value)
        if self.__head is None:
            self.__head = new

        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new

        else:
            temp = self.__head
            while (temp.next_node is not None and temp.next_node.data < value):
                temp = temp.next_node
            new.next_node = temp.next_node
            temp.next_node = new

    def __str__(self):
        string = ""
        temp = self.__head
        while temp is not None:
            string += str(temp.data)
            string += '\n'
            temp = temp.next_node
        return string[:-1]

#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import string

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None 

class DLL:
    def __init__(self):
        self.head = None

    def last(node):
        while(node.next is not None):
            last = node
            node = node.next
        return node

    def append(self, new_data):
        new_node = Node(new_data)
        new_node.next = None
        if self.head is None:
          new_node.prev = None
          self.head = new_node
          return
        last = self.head
        while(last.next is not None):
          last = last.next
        last.next = new_node
        new_node.prev = last
        return

    def find(node, value, offset, flag):
#        print("Offset= ", offset)
        listSize = 26 if flag < 1 else 10
        while(node.next is not None):
            if value == node.data:
#                print("Found= {}".format(node.data))
                break
            last = node
            node = node.next

        if offset > 0: #POSITIVE OFFSET
            for i in range(offset%listSize):
                last = node
                node = node.next
#                print("w/Offset= {}".format(node.data))
        else:          #NEGATIVE OFFSET
            offset = abs(offset)
            for i in range(offset%listSize):
                last = node
                node = node.prev
#            print("w/Offset= {}".format(node.data))

        return node.data

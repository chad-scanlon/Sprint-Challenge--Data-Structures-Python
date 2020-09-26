# from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.storage = [None] * capacity
        self.capacity = capacity
        self.new_item = 0

# make new_item zero index
# use a length method

    def append(self, item):      
        if self.new_item == (len(self.storage)):
            self.new_item = 0
            self.storage[self.new_item] = item
            self.new_item += 1
        else:
            self.storage[self.new_item] = item
            self.new_item += 1

    def get(self):
        
        # list comprehension?
        return [item for item in self.storage if item is not None]

    def __len__(self):
        return len(self.storage)


# class RingBuffer:
#     def __init__(self, capacity):
#         self.storage = DoublyLinkedList()
#         self.capacity = capacity
#         self.newest = None

#     def append(self, item):
#         if len(self.storage) == 0:
#             # check for empty list
#             self.storage.add_to_head(item)
#             self.newest = self.storage.head
#             # add to list as head          
#         elif len(self.storage) < self.capacity:
#             self.storage.add_to_tail(item)
#             # add to tail if not empty
#         elif len(self.storage) == self.capacity:

#             if self.current.next:
#                 self.current.value = item
#                 self.current = self.current.next
            
#             else: 
#                 self.current.value = item

#                 self.current = self.storage.head
#     # while loop
#     # append new value
#     def get(self):
#         contents = []

#         node = self.storage.head

#         while(node):
#             contents.append(node.value)
#             node = node.next
#         return contents




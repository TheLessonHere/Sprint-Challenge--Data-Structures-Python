from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if not self.storage.head and not self.storage.tail:
            self.storage.add_to_head(item)
            self.current = self.storage.head
        elif self.storage.length == self.capacity and self.current.next is not None:
            next_oldest = self.current.next
            self.current.value = item
            self.current = next_oldest
        elif self.storage.length == self.capacity and self.current.next is None:
            next_oldest = self.storage.head
            self.current.value = item
            self.current = next_oldest
        elif self.storage.length < self.capacity:
            self.storage.add_to_tail(item)

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        if not self.storage.head and not self.storage.tail:
            return list_buffer_contents
        elif self.storage.head.value is not None:
            self.current_node = self.storage.head
            list_buffer_contents.append(self.current_node.value)
            while self.current_node.next is not None:
                self.current_node = self.current_node.next
                list_buffer_contents.append(self.current_node.value)

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass

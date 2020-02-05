# Define node structure
class Node:
    def __init__(self, item):
        self.item = item
        self.next = None


# Singly linked list class
class SinglyLinkedList(object):
    """" Iterator method """

    def __init__(self):
        self._total_size = 0
        self._head = Node(None)  # Dummy node for iterator starting position
        self._tail = self._head

    def __iter__(self):
        self._current_index = -1
        self._current_node = self._head
        return self

    def __next__(self):
        if self._current_index + 1 >= self._total_size:
            raise StopIteration
        else:
            self._current_index += 1
            self._current_node = self._current_node.next

            return self._current_node.item

    def _find_previous_node(self, index):
        """Find the previous node from an index"""

        if index > self._total_size:
            return None

        previous_node = self._head
        index_count = index

        while index_count > 0:
            previous_node = previous_node.next
            index_count -= 1

        return previous_node

    def _tail_handling(self, index, assigning_node):
        """Update the tail node."""

        if index + 1 is self._total_size:
            self._tail = assigning_node

    def append(self, item):
        """Add an item to the end."""

        # Make a node.
        new_node = Node(item)

        # Head is None
        if self._head.next is None:
            self._head.next = new_node
            self._tail = self._head.next

        self._tail.next = new_node
        self._tail_handling(self._total_size - 1, new_node)
        self._total_size += 1

    def insert(self, index, item):
        """Insert an item at a given position."""

        # Find a position.
        previous_node = self._find_previous_node(index)

        if previous_node is None:
            return

        # Insert an item.
        new_node = Node(item)
        new_node.next = previous_node.next
        previous_node.next = new_node

        # Tail handling
        self._tail_handling(index, new_node)

        self._total_size += 1

    def remove(self, item):
        """Remove the first item from the list whose value is equal to x."""

        index = self.index(item)
        previous_node = self._find_previous_node(index)

        previous_node.next = previous_node.next.next

        # Tail handling
        self._tail_handling(index, previous_node)

        self._total_size -= 1

    def pop(self, index=-1):
        """Remove the item, and return it."""

        if index is -1:
            index = self.size() - 1

            if index < 0:
                raise IndexError(f'{index} is wrong.')

        previous_node = self._find_previous_node(index)
        item = previous_node.next.item
        previous_node.next = previous_node.next.next

        # Tail handling
        self._tail_handling(index, previous_node)

        self._total_size -= 1

        return item

    def clear(self):
        """Remove all items."""
        self._head = None
        self._tail = None
        self._total_size = 0

    def index(self, item, start=0, end=-1):
        """Find an index of a item."""

        if end is -1:
            end = self.size()

        current_node = self._head.next
        node_index = 0

        while (current_node is not None) & node_index < end:
            if start > 0:
                start -= 1
                continue

            if current_node.item is item:
                return node_index

            current_node = current_node.next
            node_index += 1

        raise ValueError(f'{item} is not in the list')

    def sort(self):
        """Sort the items of the list in place."""
        pass

    def reverse(self):
        """ Reverse the elements of the list in place."""

        next_node = None

        current_node = self._head.next

        while current_node is not None:
            prev_node = current_node.next
            current_node.next = next_node  # Attach the next node.
            next_node = current_node  # For current node -> next node(reverse) in the next loop.
            current_node = prev_node  # move the next node to repeat.

        self._head.next = self._tail

    def size(self):
        """Get node size in the linked list."""
        return self._total_size

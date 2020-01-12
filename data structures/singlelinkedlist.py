# define node structure
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# single linked list class
class SingleLinkedList:
    def __init__(self):
        self._total_size = 0
        self._head = None
        self._tail = None

    # find the previous node from an index
    def _find_previous_node(self, index):
        if index + 1 > self._total_size:
            return False

        previous_node_of_target = self._head
        index_count = index - 1

        while index_count > 0:
            previous_node_of_target = previous_node_of_target.next
            index_count -= 1

        return previous_node_of_target

    # append data into the tail of list
    def append(self, data):
        # head
        if self._head is None:
            self._head = data
        # tail
        else:
            if self._tail is not None:
                self._tail.next = data

        self._tail = data

        self._total_size += 1

    # remove node for data
    def remove(self, data):
        target_index = self.find(data)
        previous_node_of_target = self._find_previous_node(target_index)

        previous_node_of_target.next = previous_node_of_target.next.next

        self._total_size -= 1

    # find an index of a node
    def find(self, data):
        current_node = self._head
        node_index = 0

        while current_node is not None:
            if current_node.data is data:
                return node_index

            current_node = current_node.next
            node_index += 1

    # reverse list
    def reverse(self):
        next_node = None

        current_node = self._head

        while current_node is not None:
            prev_node = current_node.next
            current_node.next = next_node # 다음 노드를 붙임
            next_node = current_node # 현재 작업 노드를 다음 루프에서 next node로 붙이기 위함
            current_node = prev_node # 한칸 옮겨서 반복 작업하기 위함

        self._head = self._tail

    # get node size in the linked list
    def size(self):
        return self._total_size

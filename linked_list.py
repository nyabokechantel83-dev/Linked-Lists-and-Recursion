class Node:
    """A single node holding an integer ID and a reference to the next node."""

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """Singly linked list of employee IDs with recursive operations."""

    def __init__(self):
        self.head = None

    # ---------- Insertion ----------
    def insert_at_front(self, data):
        """O(1): the new node points at the old head and becomes the head."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        """O(n): walk to the last node, then attach the new node."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    # ---------- Sum (recursive) ----------
    def recursive_sum(self):
        return self._sum_recursive(self.head)

    def _sum_recursive(self, node):
        # Base case: past the last node, nothing left to add
        if node is None:
            return 0
        # Recursive case: this node's value + the sum of the rest
        return node.data + self._sum_recursive(node.next)

    # ---------- Reverse in place (recursive) ----------
    def recursive_reverse(self):
        self.head = self._reverse_recursive(self.head, None)

    def _reverse_recursive(self, node, prev):
        # Base case: reached the end; `prev` is the old last node = new head
        if node is None:
            return prev
        # Save the next node before overwriting the pointer
        next_node = node.next
        # Re-point this node backwards (in place, no new nodes created)
        node.next = prev
        # Recursive case: move forward, with this node as the new `prev`
        return self._reverse_recursive(next_node, node)

    # ---------- Search (recursive) ----------
    def recursive_search(self, target):
        return self._search_recursive(self.head, target)

    def _search_recursive(self, node, target):
        # Base case 1: end of the list, target not found
        if node is None:
            return False
        # Base case 2: found it
        if node.data == target:
            return True
        # Recursive case: keep looking in the rest of the list
        return self._search_recursive(node.next, target)

    # ---------- Display ----------
    def to_list(self):
        result, current = [], self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

    def __str__(self):
        return " -> ".join(str(x) for x in self.to_list()) + " -> None"
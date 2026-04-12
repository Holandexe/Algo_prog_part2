class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority
        self.left = None
        self.right = None


class BinaryTreePriorityQueue:
    def __init__(self):
        self.root = None

    def insert(self, value, priority):
        new_node = Node(value, priority)
        if self.root is None:
            self.root = new_node
        else:
            self.root = self._insert(self.root, new_node)

    def _insert(self, current, new_node):
        if current is None:
            return new_node
        if new_node.priority >= current.priority:
            current.left = self._insert(current.left, new_node)
        else:
            current.right = self._insert(current.right, new_node)
        return current

    def pop(self):
        if self.root is None:
            return None
        parent = None
        current = self.root
        while current.left is not None:
            parent = current
            current = current.left
        result = (current.value, current.priority)
        if parent is None:
            self.root = current.right
        else:
            parent.left = current.right
        return result

    def peek(self):
        if self.root is None:
            return None
        current = self.root
        while current.left is not None:
            current = current.left
        return (current.value, current.priority)

    def is_empty(self):
        return self.root is None

    def display(self):
        elements = []
        self._inorder(self.root, elements)
        print("Queue (highest to lowest priority):")
        for value, priority in elements:
            print(f"  value={value}, priority={priority}")

    def _inorder(self, node, result):
        if node is None:
            return
        self._inorder(node.left, result)
        result.append((node.value, node.priority))
        self._inorder(node.right, result)


if __name__ == "__main__":
    pq = BinaryTreePriorityQueue()

    pq.insert("task C", 3)
    pq.insert("task A", 10)
    pq.insert("task D", 1)
    pq.insert("task B", 7)
    pq.insert("task E", 5)

    pq.display()

    top = pq.peek()
    print(f"\nPeek: value={top[0]}, priority={top[1]}")

    print("\nPopping elements:")
    while not pq.is_empty():
        item = pq.pop()
        print(f"  Removed: value={item[0]}, priority={item[1]}")

    print("\nIs empty?", pq.is_empty())
import unittest
from lab4 import BinaryTreePriorityQueue


class TestBinaryTreePriorityQueue(unittest.TestCase):

    def setUp(self):
        self.pq = BinaryTreePriorityQueue()

    def test_new_queue_is_empty(self):
        self.assertTrue(self.pq.is_empty())

    def test_not_empty_after_insert(self):
        self.pq.insert("task A", 5)
        self.assertFalse(self.pq.is_empty())

    def test_peek_returns_highest_priority(self):
        self.pq.insert("task A", 3)
        self.pq.insert("task B", 10)
        self.pq.insert("task C", 1)
        value, priority = self.pq.peek()
        self.assertEqual(priority, 10)
        self.assertEqual(value, "task B")

    def test_peek_does_not_remove_element(self):
        self.pq.insert("task A", 5)
        self.pq.peek()
        self.assertFalse(self.pq.is_empty())
        self.assertEqual(self.pq.peek(), ("task A", 5))

    def test_pop_returns_highest_priority(self):
        self.pq.insert("task A", 3)
        self.pq.insert("task B", 10)
        self.pq.insert("task C", 1)
        value, priority = self.pq.pop()
        self.assertEqual(priority, 10)
        self.assertEqual(value, "task B")

    def test_pop_removes_element(self):
        self.pq.insert("task A", 5)
        self.pq.insert("task B", 9)
        self.pq.pop()
        value, priority = self.pq.peek()
        self.assertEqual(priority, 5)

    def test_pop_order_is_descending(self):
        priorities = [4, 7, 1, 9, 3]
        for i, p in enumerate(priorities):
            self.pq.insert(f"task {i}", p)
        result = []
        while not self.pq.is_empty():
            _, priority = self.pq.pop()
            result.append(priority)
        self.assertEqual(result, sorted(priorities, reverse=True))

    def test_pop_on_empty_queue_returns_none(self):
        self.assertIsNone(self.pq.pop())

    def test_peek_on_empty_queue_returns_none(self):
        self.assertIsNone(self.pq.peek())

    def test_single_element_insert_peek_pop(self):
        self.pq.insert("only", 42)
        self.assertEqual(self.pq.peek(), ("only", 42))
        self.assertEqual(self.pq.pop(), ("only", 42))
        self.assertTrue(self.pq.is_empty())

    def test_equal_priorities_all_popped(self):
        self.pq.insert("task A", 5)
        self.pq.insert("task B", 5)
        self.pq.insert("task C", 5)
        popped = []
        while not self.pq.is_empty():
            popped.append(self.pq.pop())
        self.assertEqual(len(popped), 3)
        self.assertTrue(all(p == 5 for _, p in popped))

    def test_tree_priority_rule_parent_vs_children(self):
        self.pq.insert("low", 1)
        self.pq.insert("high", 10)
        self.pq.insert("mid", 5)
        root = self.pq.root
        if root.left:
            self.assertGreaterEqual(root.left.priority, root.priority)
        if root.right:
            self.assertLess(root.right.priority, root.priority)

    def test_large_sequence(self):
        import random
        random.seed(0)
        values = list(range(50))
        random.shuffle(values)
        for v in values:
            self.pq.insert(f"task {v}", v)
        result = []
        while not self.pq.is_empty():
            _, priority = self.pq.pop()
            result.append(priority)
        self.assertEqual(result, sorted(values, reverse=True))


if __name__ == "__main__":
    unittest.main()
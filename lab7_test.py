import unittest
from lab7 import MaxFlow

class TestMaxFlow(unittest.TestCase):
    def test_simple_flow(self):
        # Тест простого лінійного шляху
        edges = [('A', 'B', 10), ('B', 'C', 5)]
        mf = MaxFlow(edges, 'A', 'C')
        self.assertEqual(mf.get_max_flow(), 5)

    def test_parallel_flow(self):
        # Тест паралельних шляхів
        edges = [('S', 'A', 10), ('S', 'B', 10), ('A', 'T', 5), ('B', 'T', 7)]
        mf = MaxFlow(edges, 'S', 'T')
        self.assertEqual(mf.get_max_flow(), 12)

    def test_bottleneck(self):
        # Тест вузького місця
        edges = [('S', 'A', 100), ('A', 'B', 10), ('B', 'T', 100)]
        mf = MaxFlow(edges, 'S', 'T')
        self.assertEqual(mf.get_max_flow(), 10)

if __name__ == '__main__':
    unittest.main()
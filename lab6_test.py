import unittest


def build_graph(roads):
    graph = {}
    for road in roads:
        u = road[0]
        v = road[1]
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append(v)
    return graph


def bfs(graph, start):
    visited = []
    queue = [start]
    visited.append(start)

    while len(queue) > 0:
        current = queue[0]
        queue = queue[1:]

        if current in graph:
            for neighbor in graph[current]:
                if neighbor not in visited:
                    visited.append(neighbor)
                    queue.append(neighbor)

    return visited


def find_unreachable(graph, sources, cities):
    result = []

    for source in sources:
        reachable = bfs(graph, source)
        unreachable = []

        for city in cities:
            if city not in reachable:
                unreachable.append(city)

        if len(unreachable) > 0:
            result.append([source, unreachable])

    return result


def find_shortest_path(graph, start, end):
    queue = [[start]]
    visited = [start]

    while len(queue) > 0:
        path = queue[0]
        queue = queue[1:]
        current = path[len(path) - 1]

        if current == end:
            return path

        if current in graph:
            for neighbor in graph[current]:
                if neighbor not in visited:
                    visited.append(neighbor)
                    new_path = []
                    for node in path:
                        new_path.append(node)
                    new_path.append(neighbor)
                    queue.append(new_path)

    return []


class TestBuildGraph(unittest.TestCase):

    def test_basic_graph(self):
        roads = [['Kyiv', 'Lviv'], ['Lviv', 'Stryi']]
        graph = build_graph(roads)
        self.assertEqual(graph['Kyiv'], ['Lviv'])
        self.assertEqual(graph['Lviv'], ['Stryi'])

    def test_all_nodes_present(self):
        roads = [['Kyiv', 'Lviv']]
        graph = build_graph(roads)
        self.assertIn('Kyiv', graph)
        self.assertIn('Lviv', graph)

    def test_empty_roads(self):
        graph = build_graph([])
        self.assertEqual(graph, {})

    def test_multiple_neighbors(self):
        roads = [['Kyiv', 'Lviv'], ['Kyiv', 'Dolyna']]
        graph = build_graph(roads)
        self.assertEqual(graph['Kyiv'], ['Lviv', 'Dolyna'])


class TestBFS(unittest.TestCase):

    def test_reachable_cities(self):
        roads = [['Kyiv', 'Lviv'], ['Lviv', 'Stryi']]
        graph = build_graph(roads)
        visited = bfs(graph, 'Kyiv')
        self.assertIn('Lviv', visited)
        self.assertIn('Stryi', visited)

    def test_start_in_visited(self):
        roads = [['Kyiv', 'Lviv']]
        graph = build_graph(roads)
        visited = bfs(graph, 'Kyiv')
        self.assertIn('Kyiv', visited)

    def test_unreachable_city(self):
        roads = [['Kyiv', 'Lviv'], ['Dolyna', 'Stryi']]
        graph = build_graph(roads)
        visited = bfs(graph, 'Kyiv')
        self.assertNotIn('Stryi', visited)

    def test_single_node(self):
        graph = {'Kyiv': []}
        visited = bfs(graph, 'Kyiv')
        self.assertEqual(visited, ['Kyiv'])


class TestFindUnreachable(unittest.TestCase):

    def test_all_reachable(self):
        roads = [['Kyiv', 'Lviv'], ['Kyiv', 'Stryi']]
        graph = build_graph(roads)
        result = find_unreachable(graph, ['Kyiv'], ['Lviv', 'Stryi'])
        self.assertEqual(result, [])

    def test_some_unreachable(self):
        roads = [['Kyiv', 'Lviv']]
        graph = build_graph(roads)
        result = find_unreachable(graph, ['Kyiv'], ['Lviv', 'Stryi'])
        self.assertEqual(result, [['Kyiv', ['Stryi']]])

    def test_multiple_sources(self):
        roads = [['Kyiv', 'Lviv'], ['Kharkiv', 'Stryi']]
        graph = build_graph(roads)
        result = find_unreachable(graph, ['Kyiv', 'Kharkiv'], ['Lviv', 'Stryi'])
        self.assertEqual(len(result), 2)

    def test_empty_cities(self):
        roads = [['Kyiv', 'Lviv']]
        graph = build_graph(roads)
        result = find_unreachable(graph, ['Kyiv'], [])
        self.assertEqual(result, [])


class TestFindShortestPath(unittest.TestCase):

    def test_direct_path(self):
        roads = [['Kyiv', 'Lviv']]
        graph = build_graph(roads)
        path = find_shortest_path(graph, 'Kyiv', 'Lviv')
        self.assertEqual(path, ['Kyiv', 'Lviv'])

    def test_longer_path(self):
        roads = [['Kyiv', 'Lviv'], ['Lviv', 'Stryi']]
        graph = build_graph(roads)
        path = find_shortest_path(graph, 'Kyiv', 'Stryi')
        self.assertEqual(path, ['Kyiv', 'Lviv', 'Stryi'])

    def test_no_path(self):
        roads = [['Kyiv', 'Lviv'], ['Dolyna', 'Stryi']]
        graph = build_graph(roads)
        path = find_shortest_path(graph, 'Kyiv', 'Stryi')
        self.assertEqual(path, [])

    def test_start_equals_end(self):
        roads = [['Kyiv', 'Lviv']]
        graph = build_graph(roads)
        path = find_shortest_path(graph, 'Kyiv', 'Kyiv')
        self.assertEqual(path, ['Kyiv'])

    def test_shortest_among_multiple(self):
        roads = [['Kyiv', 'Lviv'], ['Kyiv', 'Dolyna'], ['Dolyna', 'Stryi'], ['Lviv', 'Drohobych'], ['Drohobych', 'Stryi']]
        graph = build_graph(roads)
        path = find_shortest_path(graph, 'Kyiv', 'Stryi')
        self.assertEqual(len(path), 3)


if __name__ == '__main__':
    unittest.main()
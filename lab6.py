cities = ['Lviv', 'Stryi', 'Dolyna', 'Drohobych', 'Boryslav', 'Truskavets']
sources = ['Kyiv', 'Kharkiv']
roads = [
    ['Kyiv', 'Lviv'],
    ['Kyiv', 'Dolyna'],
    ['Lviv', 'Stryi'],
    ['Lviv', 'Drohobych'],
    ['Dolyna', 'Stryi'],
    ['Drohobych', 'Boryslav'],
    ['Kharkiv', 'Drohobych'],
    ['Kharkiv', 'Truskavets']
]


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


graph = build_graph(roads)

print("=== City Route System ===")
print()
print("Available cities: " + str(cities))
print("Available sources: " + str(sources))
print()
print("Choose task:")
print("1 - Show unreachable cities from each source")
print("2 - Find shortest path between two cities")

choice = input("Your choice (1 or 2): ")

if choice == "1":
    print()
    print("=== Unreachable cities ===")
    result = find_unreachable(graph, sources, cities)

    if len(result) == 0:
        print("All sources can reach all cities.")
    else:
        for entry in result:
            print(entry[0] + " cannot reach: " + str(entry[1]))

elif choice == "2":
    print()
    print("Choose start city:")
    all_nodes = sources + cities
    for i in range(len(all_nodes)):
        print(str(i + 1) + " - " + all_nodes[i])

    start_index = int(input("Enter number: ")) - 1
    start = all_nodes[start_index]

    print()
    print("Choose destination city:")
    for i in range(len(cities)):
        print(str(i + 1) + " - " + cities[i])

    end_index = int(input("Enter number: ")) - 1
    end = cities[end_index]

    print()
    path = find_shortest_path(graph, start, end)

    if len(path) == 0:
        print("No path found from " + start + " to " + end)
    else:
        print("Shortest path: " + " -> ".join(path))
        print("Steps: " + str(len(path) - 1))

else:
    print("Invalid choice.")
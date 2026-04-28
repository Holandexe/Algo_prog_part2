cities = ['Київ', 'Харків', 'Львів', 'Стрий', 'Долина', 'Дрогобич', 'Борислав', 'Трускавець']
sources = ['Київ', 'Харків', 'Львів', 'Стрий']
roads = [
    ['Київ', 'Львів'],
    ['Київ', 'Долина'],
    ['Львів', 'Стрий'],
    ['Львів', 'Дрогобич'],
    ['Долина', 'Стрий'],
    ['Дрогобич', 'Борислав'],
    ['Харків', 'Дрогобич'],
    ['Харків', 'Трускавець']
]

def build_graph(roads):
    graph = {}
    for road in roads:
        u, v = road[0], road[1]
        if u not in graph: graph[u] = []
        if v not in graph: graph[v] = []
        graph[u].append(v)
        graph[v].append(u)
    return graph

def bfs(graph, start):
    visited = []
    queue = [start]
    visited.append(start)
    while len(queue) > 0:
        current = queue.pop(0)
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
        unreachable = [city for city in cities if city not in reachable]
        if len(unreachable) > 0:
            result.append([source, unreachable])
    return result

def find_shortest_path(graph, start, end):
    queue = [[start]]
    visited = [start]
    while len(queue) > 0:
        path = queue.pop(0)
        current = path[-1]
        if current == end:
            return path
        if current in graph:
            for neighbor in graph[current]:
                if neighbor not in visited:
                    visited.append(neighbor)
                    new_path = list(path)
                    new_path.append(neighbor)
                    queue.append(new_path)
    return []

graph = build_graph(roads)
task_1_completed = False

while True:
    print("\n=== Система маршрутів між містами ===")
    print("Доступні міста: " + str(cities))
    print("Доступні джерела: " + str(sources))
    print("\nОберіть завдання:")
    print("1 - Показати недосяжні міста з кожного джерела")
    print("2 - Знайти найкоротший шлях між двома містами")
    print("0 - Вийти")

    choice = input("Ваш вибір: ")

    if choice == "1":
        if task_1_completed:
            raise Exception("Помилка: Ви вже обирали пункт 1!")

        print("\n=== Недосяжні міста ===")
        result = find_unreachable(graph, sources, cities)
        if len(result) == 0:
            print("Усі джерела можуть дістатися до всіх міст.")
        else:
            for entry in result:
                print(entry[0] + " не може дістатися до: " + str(entry[1]))
        task_1_completed = True

    elif choice == "2":
        all_nodes = sources + cities
        print("\nОберіть місто відправлення:")
        for i, node in enumerate(all_nodes):
            print(f"{i + 1} - {node}")
        start = all_nodes[int(input("Введіть номер: ")) - 1]

        print("\nОберіть місто призначення:")
        for i, city in enumerate(cities):
            print(f"{i + 1} - {city}")
        end = cities[int(input("Введіть номер: ")) - 1]

        path = find_shortest_path(graph, start, end)
        if not path:
            print(f"\nШлях від {start} до {end} не знайдено")
        else:
            print("\nНайкоротший шлях: " + " -> ".join(path))
            print("Кількість кроків: " + str(len(path) - 1))

    elif choice == "0":
        break
    else:
        print("Невірний вибір.")
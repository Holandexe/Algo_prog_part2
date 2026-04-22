class Queue:
    def __init__(self):
        self.data = []
        self.head = 0

    def enqueue(self, item):
        self.data.append(item)

    def dequeue(self):
        item = self.data[self.head]
        self.head += 1
        return item

    def is_empty(self):
        return self.head >= len(self.data)


def read_input(filename):
    try:
        file = open(filename, 'r')
        lines = []
        for line in file:
            if '#' in line:
                line = line[:line.index('#')]
            
            stripped = line.strip()
            if stripped != '':
                lines.append(stripped)
        file.close()

        if len(lines) == 0:
            return None, {}

        root = int(lines[0])
        edges = {}
        i = 1
        while i < len(lines):
            parts = lines[i].split(',')
            if len(parts) == 2:
                parent = int(parts[0].strip())
                child = int(parts[1].strip())
                
                if parent not in edges:
                    edges[parent] = []
                edges[parent].append(child)
            i += 1

        return root, edges
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        print(f"Creating a sample '{filename}' for you...")

        sample_file = open(filename, 'w')
        sample_file.write("1\n1,2\n1,3\n2,4\n")
        sample_file.close()
        return read_input(filename)


def find_min_depth(root, edges):
    if root is None:
        return 0

    queue = Queue()
    # Storing tuple: (node, current_depth)
    queue.enqueue((root, 1))

    visited = {}
    visited[root] = True

    while not queue.is_empty():
        node, depth = queue.dequeue()

        children = []
        if node in edges:
            children = edges[node]

        if len(children) == 0:
            return depth

        for child in children:
            if child not in visited:
                visited[child] = True
                queue.enqueue((child, depth + 1))

    return 0


def write_output(filename, result):
    file = open(filename, 'w')
    file.write(str(result) + '\n')
    file.close()


if __name__ == '__main__':
    input_file = 'input.txt'
    output_file = 'output.txt'
    
    root, edges = read_input(input_file)
    
    if root is not None:
        result = find_min_depth(root, edges)
        write_output(output_file, result)
        print(f"Minimum depth found: {result}")
        print(f"Result has been saved to {output_file}")
    else:
        print("The input file is empty or invalid.")
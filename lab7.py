def read_data(filename):
    f = open(filename, 'r', encoding='utf-8')
    lines = f.readlines()
    f.close()
    
    clean_lines = []
    for line in lines:
        stripped = line.strip()
        if stripped:
            clean_lines.append(stripped)
            
    farms = []
    for x in clean_lines[0].split(','):
        farms.append(x.strip())
        
    shops = []
    for x in clean_lines[1].split(','):
        shops.append(x.strip())
        
    edges = []
    for i in range(2, len(clean_lines)):
        parts = clean_lines[i].split(',')
        if len(parts) == 3:
            edges.append((parts[0].strip(), parts[1].strip(), int(parts[2].strip())))
            
    return farms, shops, edges

class MaxFlow:
    def __init__(self, edges, source, sink):
        self.graph = {}
        self.nodes = set()
        for u, v, cap in edges:
            self.add_edge(u, v, cap)
            self.nodes.add(u)
            self.nodes.add(v)
        self.source = source
        self.sink = sink

    def add_edge(self, u, v, cap):
        if u not in self.graph: self.graph[u] = {}
        if v not in self.graph: self.graph[v] = {}
        
        current_cap = self.graph[u].get(v, 0)
        self.graph[u][v] = current_cap + cap
        
        if u not in self.graph[v]:
            self.graph[v][u] = 0

    def bfs(self, parent):
        visited = {}
        for node in self.nodes:
            visited[node] = False
            
        queue = [self.source]
        visited[self.source] = True
        
        while len(queue) > 0:
            u = queue.pop(0)
            if u in self.graph:
                for v, cap in self.graph[u].items():
                    if not visited.get(v, False) and cap > 0:
                        queue.append(v)
                        visited[v] = True
                        parent[v] = u
                        if v == self.sink:
                            return True
        return False

    def get_max_flow(self):
        parent = {}
        max_f = 0
        while self.bfs(parent):
            path_flow = 10**18 
            s = self.sink
            while s != self.source:
                val = self.graph[parent[s]][s]
                if val < path_flow:
                    path_flow = val
                s = parent[s]
            
            max_f += path_flow
            v = self.sink
            while v != self.source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]
        return max_f

def solve():
    farms, shops, edges = read_data('roads.csv')
    
    super_source = 'SS_START'
    super_sink = 'SS_END'
    
    all_edges = []
    inf_val = 10**18
    
    for f in farms:
        all_edges.append((super_source, f, inf_val))
    for s in shops:
        all_edges.append((s, super_sink, inf_val))
    
    for e in edges:
        all_edges.append(e)
    
    mf = MaxFlow(all_edges, super_source, super_sink)
    return mf.get_max_flow()

if __name__ == "__main__":
    result = solve()
    print(result)
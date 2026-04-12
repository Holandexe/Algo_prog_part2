import os

class Node:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

def manual_to_int(s):
    res = 0
    is_negative = False
    start = 0
    if s[0] == "-":
        is_negative = True
        start = 1
    i = start
    while i < len(s):
        res = res * 10 + (ord(s[i]) - 48)
        i += 1
    if is_negative:
        return -res
    return res

def manual_split(text):
    words = []
    current_word = ""
    i = 0
    while i < len(text):
        c = text[i]
        if c == " " or c == "\n" or c == "\t" or c == "\r":
            if current_word != "":
                words = words + [current_word]
                current_word = ""
        else:
            current_word = current_word + c
        i += 1
    if current_word != "":
        words = words + [current_word]
    return words

def load_data(filename):
    dir_path = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.join(dir_path, filename)
    f = open(full_path, "r")
    content = f.read()
    f.close()
    return manual_split(content)

def deserialize_manual(data, index_wrapper):
    if index_wrapper[0] >= len(data):
        return None
    val = data[index_wrapper[0]]
    index_wrapper[0] += 1
    if val == "N":
        return None
    node = Node(manual_to_int(val))
    node.left = deserialize_manual(data, index_wrapper)
    node.right = deserialize_manual(data, index_wrapper)
    return node

def get_height(node):
    if node is None:
        return 0
    l = get_height(node.left)
    r = get_height(node.right)
    if l > r:
        return l + 1
    return r + 1

def int_to_str(v):
    if v == 0:
        return "0"
    s = ""
    temp = v
    if temp < 0:
        temp = -temp
    while temp > 0:
        d = temp % 10
        s = chr(d + 48) + s
        temp = temp // 10
    if v < 0:
        s = "-" + s
    return s

def assign_x(node, counter, positions):
    if node is None:
        return
    assign_x(node.left, counter, positions)
    positions[id(node)] = counter[0]
    counter[0] += 1
    assign_x(node.right, counter, positions)

def print_tree(root):
    if root is None:
        return

    h = get_height(root)
    positions = {}
    assign_x(root, [0], positions)

    SCALE = 6
    rows = h * 3

    max_x = 0
    for k in positions:
        if positions[k] > max_x:
            max_x = positions[k]

    W = (max_x + 1) * SCALE + 4

    grid = []
    i = 0
    while i < rows:
        row = []
        j = 0
        while j < W:
            row = row + [" "]
            j += 1
        grid = grid + [row]
        i += 1

    def place(s, r, c):
        start = c - len(s) // 2
        i = 0
        while i < len(s):
            x = start + i
            if x >= 0 and x < W:
                grid[r][x] = s[i]
            i += 1

    def draw_line(r1, c1, r2, c2, ch):
        dr = 1
        dc = 1
        if c2 < c1:
            dc = -1
        r = r1 + 1
        c = c1 + dc
        while r < r2:
            grid[r][c] = ch
            r += 1
            c += dc

    def fill(node, depth):
        if node is None:
            return

        col = positions[id(node)]
        row = depth * 2

        place(int_to_str(node.val), row, col)

        if node.left is not None:
            lc = positions[id(node.left)]
            draw_line(row, col, row + 2, lc, "/")

        if node.right is not None:
            rc = positions[id(node.right)]
            draw_line(row, col, row + 2, rc, "\\")

        fill(node.left, depth + 1)
        fill(node.right, depth + 1)

    fill(root, 0)

    i = 0
    while i < rows:
        line = ""
        j = 0
        last = -1
        while j < W:
            line = line + grid[i][j]
            if grid[i][j] != " ":
                last = j
            j += 1
        if last >= 0:
            k = 0
            out = ""
            while k <= last:
                out = out + line[k]
                k += 1
            print(out)
        i += 1


data_list = load_data("tree.txt")
tree = deserialize_manual(data_list, [0])
print_tree(tree)
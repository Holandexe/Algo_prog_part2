class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def invert_binary_tree(tree) -> BinaryTree:
    if tree is None:
        return None
    tree.left, tree.right = invert_binary_tree(tree.right), invert_binary_tree(tree.left)
    return tree


def print_tree(root):
    if root is None:
        print("Дерево порожнє")
        return

    def build(node):
        if node is None:
            return [""], 0

        val = str(node.value)
        if not node.left and not node.right:
            return [val], len(val) // 2

        left_block,  lc = build(node.left)  if node.left  else ([""], 0)
        right_block, rc = build(node.right) if node.right else ([""], 0)

        lw = max(len(l) for l in left_block)
        rw = max(len(l) for l in right_block)

        left_block  = [l.ljust(lw) for l in left_block]
        right_block = [r.ljust(rw) for r in right_block]

        gap = 2
        root_pos = lw + gap
        total_w  = lw + gap + len(val) + gap + rw

        top      = " " * root_pos + val
        slashes  = " " * lc + "/" + " " * (root_pos - lc - 1 + len(val) + gap + rc) + "\\"

        if not node.left:
            slashes = " " * (root_pos + len(val) + gap + rc) + "\\"
            top     = " " * root_pos + val
        if not node.right:
            slashes = " " * lc + "/"
            top     = " " * root_pos + val

        depth = max(len(left_block), len(right_block))
        left_block  += [""] * (depth - len(left_block))
        right_block += [""] * (depth - len(right_block))

        children = []
        for l, r in zip(left_block, right_block):
            children.append(l.ljust(lw) + " " * (gap + len(val) + gap) + r)

        lines = [top, slashes] + children
        return lines, root_pos

    lines, _ = build(root)
    for line in lines:
        print(line)


if __name__ == "__main__":
    root = BinaryTree(1)
    root.left, root.right = BinaryTree(2), BinaryTree(3)
    root.left.left, root.left.right = BinaryTree(4), BinaryTree(5)
    root.right.left, root.right.right = BinaryTree(6), BinaryTree(7)

    print("Оригінальне дерево:")
    print_tree(root)
    invert_binary_tree(root)
    print("\nІнвертоване дерево:")
    print_tree(root)
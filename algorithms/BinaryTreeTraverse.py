from datastruct.BinaryTree import Node


def traverse(root):
    if root is None:
        return
    # 前序位置
    print(f"前序位置: {root.value}")
    traverse(root.left)
    # 中序位置
    print(f"中序位置: {root.value}")
    traverse(root.right)
    print(f"后序位置: {root.value}")
    # 后序位置


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    traverse(root)
